"""
Unit tests for vector store and index manager.
"""

import pytest
import numpy as np
import tempfile
import shutil
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.index.vector_store import VectorStore
from scripts.index.manager import IndexManager


class TestVectorStore:
    """Test cases for VectorStore."""
    
    def test_initialization(self):
        """Test vector store initialization."""
        store = VectorStore(dimension=512)
        
        assert store.dimension == 512
        assert store.n_connections == 32
        assert store.get_vector_count() == 0
    
    def test_add_vectors(self):
        """Test adding vectors to the store."""
        store = VectorStore(dimension=512)
        
        vectors = np.random.rand(10, 512).astype(np.float32)
        metadata = [{'id': i} for i in range(10)]
        chunks = [f'chunk_{i}' for i in range(10)]
        
        n_added = store.add_vectors(vectors, metadata, chunks)
        
        assert n_added == 10
        assert store.get_vector_count() == 10
    
    def test_search(self):
        """Test vector search."""
        store = VectorStore(dimension=512)
        
        # Add some vectors
        vectors = np.random.rand(10, 512).astype(np.float32)
        metadata = [{'id': i} for i in range(10)]
        store.add_vectors(vectors, metadata)
        
        # Search with first vector
        query = vectors[0:1]
        distances, indices, meta = store.search(query, top_k=5)
        
        assert distances.shape[0] == 1
        assert indices.shape[0] == 1
        assert len(meta) == 1
    
    def test_save_and_load(self):
        """Test saving and loading index."""
        store = VectorStore(dimension=512)
        
        # Add vectors
        vectors = np.random.rand(5, 512).astype(np.float32)
        metadata = [{'id': i} for i in range(5)]
        chunks = [f'chunk_{i}' for i in range(5)]
        store.add_vectors(vectors, metadata, chunks)
        
        # Save to temp directory
        temp_dir = tempfile.mkdtemp()
        try:
            success = store.save(temp_dir)
            assert success
            
            # Load into new store
            new_store = VectorStore(dimension=512)
            success = new_store.load(temp_dir)
            
            assert success
            assert new_store.get_vector_count() == 5
        finally:
            shutil.rmtree(temp_dir)
    
    def test_get_metadata(self):
        """Test getting metadata."""
        store = VectorStore(dimension=512)
        
        vectors = np.random.rand(3, 512).astype(np.float32)
        metadata = [{'id': i, 'title': f'doc_{i}'} for i in range(3)]
        store.add_vectors(vectors, metadata)
        
        meta = store.get_metadata(1)
        assert meta['id'] == 1
        assert meta['title'] == 'doc_1'
    
    def test_get_chunk(self):
        """Test getting chunk text."""
        store = VectorStore(dimension=512)
        
        vectors = np.random.rand(3, 512).astype(np.float32)
        chunks = ['chunk_0', 'chunk_1', 'chunk_2']
        store.add_vectors(vectors, chunks=chunks)
        
        chunk = store.get_chunk(1)
        assert chunk == 'chunk_1'
    
    def test_clear(self):
        """Test clearing the store."""
        store = VectorStore(dimension=512)
        
        vectors = np.random.rand(5, 512).astype(np.float32)
        store.add_vectors(vectors)
        
        store.clear()
        
        assert store.get_vector_count() == 0
        assert len(store.metadata_store) == 0
    
    def test_get_stats(self):
        """Test getting statistics."""
        store = VectorStore(dimension=512)
        
        vectors = np.random.rand(5, 512).astype(np.float32)
        store.add_vectors(vectors)
        
        stats = store.get_stats()
        
        assert stats['total_vectors'] == 5
        assert stats['dimension'] == 512


class TestIndexManager:
    """Test cases for IndexManager."""
    
    def test_initialization(self):
        """Test index manager initialization."""
        manager = IndexManager('.test-index')
        
        assert manager.index_path == '.test-index'
    
    def test_build_index(self):
        """Test building an index."""
        manager = IndexManager('.test-index')
        
        vectors = np.random.rand(10, 512).astype(np.float32)
        metadata = [{'id': i} for i in range(10)]
        chunks = [f'chunk_{i}' for i in range(10)]
        
        result = manager.build_index(vectors, metadata, chunks)
        
        assert result['success']
        assert result['total_vectors'] == 10
    
    def test_save_and_load(self):
        """Test saving and loading index."""
        temp_dir = tempfile.mkdtemp()
        
        try:
            manager = IndexManager(temp_dir)
            
            # Build and save
            vectors = np.random.rand(5, 512).astype(np.float32)
            metadata = [{'id': i} for i in range(5)]
            chunks = [f'chunk_{i}' for i in range(5)]
            
            manager.build_index(vectors, metadata, chunks)
            success = manager.save_index()
            assert success
            
            # Load in new manager
            new_manager = IndexManager(temp_dir)
            success = new_manager.load_index()
            
            assert success
            stats = new_manager.get_stats()
            assert stats['total_vectors'] == 5
        
        finally:
            shutil.rmtree(temp_dir)
    
    def test_search(self):
        """Test searching with manager."""
        manager = IndexManager('.test-search')
        
        vectors = np.random.rand(10, 512).astype(np.float32)
        metadata = [{'id': i, 'category': 'test'} for i in range(10)]
        chunks = [f'chunk_{i}' for i in range(10)]
        
        manager.build_index(vectors, metadata, chunks)
        
        # Search
        query = vectors[0:1]
        results = manager.search(query, top_k=5)
        
        assert len(results) > 0
        assert 'similarity' in results[0]
        assert 'metadata' in results[0]
        
        # Cleanup
        shutil.rmtree('.test-search', ignore_errors=True)
    
    def test_index_exists(self):
        """Test checking if index exists."""
        temp_dir = tempfile.mkdtemp()
        
        try:
            manager = IndexManager(temp_dir)
            
            assert not manager.index_exists()
            
            # Create index
            vectors = np.random.rand(5, 512).astype(np.float32)
            manager.build_index(vectors, [], [])
            manager.save_index()
            
            assert manager.index_exists()
        
        finally:
            shutil.rmtree(temp_dir)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
