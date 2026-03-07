"""
Text encoder for semantic embeddings.

Provides text chunking and batch encoding capabilities.
"""

from sentence_transformers import SentenceTransformer
from typing import List, Dict, Tuple, Optional
import numpy as np
import logging

from .models import get_embedding_model, MODEL_DIMENSION

logger = logging.getLogger(__name__)


class EmbeddingEncoder:
    """
    Encoder for generating text embeddings.
    
    Handles text chunking and batch encoding for efficient processing.
    
    Attributes:
        model: SentenceTransformer model instance
        chunk_size: Maximum characters per chunk
        chunk_overlap: Overlap between consecutive chunks
        batch_size: Number of texts to encode in parallel
    
    Example:
        >>> encoder = EmbeddingEncoder()
        >>> embeddings = encoder.encode_documents(['文本1', '文本2'])
        >>> print(embeddings.shape)
        (2, 512)
    """
    
    def __init__(
        self,
        model_name: str = 'BAAI/bge-small-zh-v1.5',
        chunk_size: int = 256,
        chunk_overlap: int = 50,
        batch_size: int = 8,
        cache_dir: Optional[str] = None,
        device: str = 'cpu'
    ):
        """
        Initialize the encoder.
        
        Args:
            model_name: Name or path of the embedding model
            chunk_size: Maximum characters per chunk (default: 256)
            chunk_overlap: Character overlap between chunks (default: 50)
            batch_size: Batch size for encoding (default: 8)
            cache_dir: Directory to cache models
            device: Device to run model on ('cpu' or 'cuda')
        """
        self.model = get_embedding_model(model_name, cache_dir, device)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.batch_size = batch_size
        self.dimension = MODEL_DIMENSION
        
        logger.info(
            f"Encoder initialized: chunk_size={chunk_size}, "
            f"overlap={chunk_overlap}, batch_size={batch_size}"
        )
    
    def chunk_text(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks.
        
        Args:
            text: Input text to chunk
        
        Returns:
            List of text chunks
        
        Example:
            >>> encoder = EmbeddingEncoder(chunk_size=100, chunk_overlap=20)
            >>> chunks = encoder.chunk_text("很长的文本...")
            >>> print(len(chunks))
            5
        """
        if not text or len(text.strip()) == 0:
            return []
        
        chunks = []
        start = 0
        
        while start < len(text):
            # Get chunk end position
            end = start + self.chunk_size
            
            # Adjust for last chunk
            if end >= len(text):
                chunk = text[start:]
                if len(chunk.strip()) > 0:
                    chunks.append(chunk)
                break
            
            # Try to break at sentence boundary
            chunk = text[start:end]
            
            # Look for sentence endings (Chinese punctuation)
            for delimiter in ['。', '！', '？', '；', '\n']:
                last_delim = chunk.rfind(delimiter)
                if last_delim > len(chunk) * 0.5:  # At least halfway
                    end = start + last_delim + 1
                    chunk = text[start:end]
                    break
            
            if len(chunk.strip()) > 0:
                chunks.append(chunk)
            
            # Move to next chunk with overlap
            start = end - self.chunk_overlap
            if start < 0:
                start = 0
        
        return chunks
    
    def encode_texts(
        self,
        texts: List[str],
        show_progress: bool = False
    ) -> np.ndarray:
        """
        Encode a list of texts into embeddings.
        
        Args:
            texts: List of text strings to encode
            show_progress: Whether to show progress bar
        
        Returns:
            Numpy array of embeddings with shape (n_texts, dimension)
        
        Example:
            >>> encoder = EmbeddingEncoder()
            >>> embeddings = encoder.encode_texts(['文本1', '文本2'])
            >>> print(embeddings.shape)
            (2, 512)
        """
        if not texts:
            return np.array([]).reshape(0, self.dimension)
        
        logger.debug(f"Encoding {len(texts)} texts...")
        
        # Batch encoding
        all_embeddings = []
        
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i:i + self.batch_size]
            embeddings = self.model.encode(
                batch,
                show_progress_bar=show_progress and len(texts) > 100,
                convert_to_numpy=True
            )
            all_embeddings.append(embeddings)
        
        # Stack all embeddings
        if len(all_embeddings) == 1:
            return all_embeddings[0]
        
        return np.vstack(all_embeddings)
    
    def encode_documents(
        self,
        documents: List[Dict],
        show_progress: bool = False
    ) -> Tuple[np.ndarray, List[Dict]]:
        """
        Encode documents with chunking.
        
        Args:
            documents: List of document dicts with 'content' and 'metadata'
            show_progress: Whether to show progress bar
        
        Returns:
            Tuple of (embeddings array, chunk metadata list)
        
        Example:
            >>> encoder = EmbeddingEncoder()
            >>> docs = [{'content': '文本', 'metadata': {'id': 1}}]
            >>> embeddings, metadata = encoder.encode_documents(docs)
            >>> print(embeddings.shape[0])
            1
        """
        all_chunks = []
        chunk_metadata = []
        
        # Process each document
        for doc in documents:
            content = doc.get('content', '')
            metadata = doc.get('metadata', {})
            
            # Chunk the document
            chunks = self.chunk_text(content)
            
            for chunk in chunks:
                all_chunks.append(chunk)
                chunk_metadata.append(metadata)
        
        logger.info(
            f"Created {len(all_chunks)} chunks from {len(documents)} documents"
        )
        
        # Encode all chunks
        embeddings = self.encode_texts(all_chunks, show_progress)
        
        return embeddings, chunk_metadata
    
    def encode_query(self, query: str) -> np.ndarray:
        """
        Encode a single query text.
        
        Args:
            query: Query text string
        
        Returns:
            Query embedding with shape (1, dimension)
        
        Example:
            >>> encoder = EmbeddingEncoder()
            >>> embedding = encoder.encode_query('搜索查询')
            >>> print(embedding.shape)
            (1, 512)
        """
        if not query or len(query.strip()) == 0:
            # Return zero vector for empty query
            return np.zeros((1, self.dimension), dtype=np.float32)
        
        embedding = self.model.encode([query], convert_to_numpy=True)
        return embedding
    
    def get_dimension(self) -> int:
        """
        Get the embedding dimension.
        
        Returns:
            Embedding dimension (512 for bge-small-zh-v1.5)
        """
        return self.dimension
