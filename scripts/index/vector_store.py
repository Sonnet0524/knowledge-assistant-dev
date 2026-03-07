"""
Vector store using FAISS for efficient similarity search.

Provides HNSW-based vector indexing and retrieval.
"""

import faiss
import numpy as np
import os
import json
from typing import List, Dict, Optional, Tuple
import logging

logger = logging.getLogger(__name__)


class VectorStore:
    """
    FAISS-based vector store for semantic search.
    
    Uses HNSW (Hierarchical Navigable Small World) index for fast
    approximate nearest neighbor search.
    
    Attributes:
        dimension: Vector dimension
        n_connections: HNSW connections per node (M parameter)
        index: FAISS index instance
        metadata_store: List of metadata for each vector
    
    Example:
        >>> store = VectorStore(dimension=512)
        >>> vectors = np.random.rand(100, 512).astype('float32')
        >>> store.add_vectors(vectors)
        >>> results = store.search(vectors[0:1], top_k=5)
    """
    
    def __init__(
        self,
        dimension: int = 512,
        n_connections: int = 32
    ):
        """
        Initialize the vector store.
        
        Args:
            dimension: Vector dimension (default: 512 for bge-small-zh)
            n_connections: HNSW M parameter - connections per node (default: 32)
        """
        self.dimension = dimension
        self.n_connections = n_connections
        
        # Create HNSW index
        # M: number of connections per node
        # IndexHNSWFlat uses inner product (IP) similarity
        self.index = faiss.IndexHNSWFlat(dimension, n_connections)
        
        # HNSW parameters
        self.index.hnsw.efSearch = 32  # Search depth
        self.index.hnsw.efConstruction = 40  # Construction depth
        
        # Metadata storage
        self.metadata_store: List[Dict] = []
        self.chunk_store: List[str] = []
        
        logger.info(
            f"VectorStore initialized: dimension={dimension}, "
            f"connections={n_connections}"
        )
    
    def add_vectors(
        self,
        vectors: np.ndarray,
        metadata: Optional[List[Dict]] = None,
        chunks: Optional[List[str]] = None
    ) -> int:
        """
        Add vectors to the index.
        
        Args:
            vectors: Numpy array of vectors with shape (n, dimension)
            metadata: Optional list of metadata dicts for each vector
            chunks: Optional list of text chunks for each vector
        
        Returns:
            Number of vectors added
        
        Example:
            >>> store = VectorStore(512)
            >>> vectors = np.random.rand(10, 512).astype('float32')
            >>> n = store.add_vectors(vectors)
            >>> print(n)
            10
        """
        if len(vectors) == 0:
            return 0
        
        # Ensure float32 type
        if vectors.dtype != np.float32:
            vectors = vectors.astype(np.float32)
        
        # Add to index
        n_added = self.index.ntotal
        self.index.add(vectors)
        n_total = self.index.ntotal
        
        # Store metadata
        if metadata:
            self.metadata_store.extend(metadata)
        else:
            # Add empty metadata
            self.metadata_store.extend([{}] * len(vectors))
        
        # Store chunks
        if chunks:
            self.chunk_store.extend(chunks)
        else:
            self.chunk_store.extend([''] * len(vectors))
        
        logger.debug(f"Added {n_total - n_added} vectors. Total: {n_total}")
        
        return n_total - n_added
    
    def search(
        self,
        query_vectors: np.ndarray,
        top_k: int = 5,
        threshold: Optional[float] = None
    ) -> Tuple[np.ndarray, np.ndarray, List[Dict]]:
        """
        Search for similar vectors.
        
        Args:
            query_vectors: Query vectors with shape (n_queries, dimension)
            top_k: Number of results to return per query
            threshold: Optional similarity threshold (not used in HNSW)
        
        Returns:
            Tuple of (distances, indices, metadata_list)
        
        Example:
            >>> store = VectorStore(512)
            >>> # Add some vectors...
            >>> query = np.random.rand(1, 512).astype('float32')
            >>> distances, indices, metadata = store.search(query, top_k=5)
        """
        if self.index.ntotal == 0:
            return (
                np.array([]).reshape(0, 0),
                np.array([]).reshape(0, 0),
                []
            )
        
        # Ensure float32
        if query_vectors.dtype != np.float32:
            query_vectors = query_vectors.astype(np.float32)
        
        # Search
        distances, indices = self.index.search(query_vectors, top_k)
        
        # Get metadata for results
        metadata_list = []
        for idx_array in indices:
            meta = [self.metadata_store[i] for i in idx_array if i >= 0]
            metadata_list.append(meta)
        
        return distances, indices, metadata_list
    
    def get_vector_count(self) -> int:
        """
        Get the number of vectors in the index.
        
        Returns:
            Number of vectors
        """
        return self.index.ntotal
    
    def get_metadata(self, index: int) -> Optional[Dict]:
        """
        Get metadata for a specific vector index.
        
        Args:
            index: Vector index
        
        Returns:
            Metadata dict or None if index out of range
        """
        if 0 <= index < len(self.metadata_store):
            return self.metadata_store[index]
        return None
    
    def get_chunk(self, index: int) -> Optional[str]:
        """
        Get text chunk for a specific vector index.
        
        Args:
            index: Vector index
        
        Returns:
            Text chunk or None if index out of range
        """
        if 0 <= index < len(self.chunk_store):
            return self.chunk_store[index]
        return None
    
    def save(self, index_path: str) -> bool:
        """
        Save the vector store to disk.
        
        Args:
            index_path: Directory path to save the index
        
        Returns:
            True if successful
        
        Example:
            >>> store = VectorStore(512)
            >>> # Add vectors...
            >>> store.save('.ka-index')
        """
        try:
            os.makedirs(index_path, exist_ok=True)
            
            # Save FAISS index
            index_file = os.path.join(index_path, 'index.faiss')
            faiss.write_index(self.index, index_file)
            
            # Save metadata and chunks
            meta_file = os.path.join(index_path, 'metadata.json')
            with open(meta_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'dimension': self.dimension,
                    'n_connections': self.n_connections,
                    'metadata_store': self.metadata_store,
                    'chunk_store': self.chunk_store
                }, f, ensure_ascii=False, indent=2)
            
            logger.info(f"VectorStore saved to {index_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save VectorStore: {e}")
            return False
    
    def load(self, index_path: str) -> bool:
        """
        Load the vector store from disk.
        
        Args:
            index_path: Directory path containing saved index
        
        Returns:
            True if successful
        
        Example:
            >>> store = VectorStore(512)
            >>> store.load('.ka-index')
        """
        try:
            # Load FAISS index
            index_file = os.path.join(index_path, 'index.faiss')
            if not os.path.exists(index_file):
                logger.error(f"Index file not found: {index_file}")
                return False
            
            self.index = faiss.read_index(index_file)
            
            # Load metadata and chunks
            meta_file = os.path.join(index_path, 'metadata.json')
            with open(meta_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.dimension = data.get('dimension', self.dimension)
                self.n_connections = data.get('n_connections', self.n_connections)
                self.metadata_store = data.get('metadata_store', [])
                self.chunk_store = data.get('chunk_store', [])
            
            logger.info(
                f"VectorStore loaded from {index_path}. "
                f"Vectors: {self.index.ntotal}"
            )
            return True
            
        except Exception as e:
            logger.error(f"Failed to load VectorStore: {e}")
            return False
    
    def clear(self) -> None:
        """
        Clear all vectors and metadata from the store.
        """
        # Recreate index
        self.index = faiss.IndexHNSWFlat(self.dimension, self.n_connections)
        self.index.hnsw.efSearch = 32
        self.index.hnsw.efConstruction = 40
        
        # Clear metadata
        self.metadata_store = []
        self.chunk_store = []
        
        logger.info("VectorStore cleared")
    
    def get_stats(self) -> Dict:
        """
        Get statistics about the vector store.
        
        Returns:
            Dictionary with store statistics
        """
        return {
            'total_vectors': self.index.ntotal,
            'dimension': self.dimension,
            'n_connections': self.n_connections,
            'metadata_count': len(self.metadata_store),
            'chunk_count': len(self.chunk_store)
        }
