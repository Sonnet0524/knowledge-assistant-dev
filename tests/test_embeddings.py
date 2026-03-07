"""
Unit tests for embeddings module.
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.embeddings.encoder import EmbeddingEncoder
from scripts.embeddings.models import get_embedding_model, clear_model_cache


class TestEmbeddingEncoder:
    """Test cases for EmbeddingEncoder."""
    
    def test_encoder_initialization(self):
        """Test encoder initializes correctly."""
        encoder = EmbeddingEncoder()
        
        assert encoder.dimension == 512
        assert encoder.chunk_size == 256
        assert encoder.chunk_overlap == 50
        assert encoder.batch_size == 8
    
    def test_chunk_text_simple(self):
        """Test basic text chunking."""
        encoder = EmbeddingEncoder(chunk_size=100, chunk_overlap=20)
        
        text = "这是第一句话。这是第二句话。这是第三句话。"
        chunks = encoder.chunk_text(text)
        
        assert len(chunks) > 0
        assert all(isinstance(chunk, str) for chunk in chunks)
    
    def test_chunk_text_empty(self):
        """Test chunking empty text."""
        encoder = EmbeddingEncoder()
        
        chunks = encoder.chunk_text("")
        assert chunks == []
        
        chunks = encoder.chunk_text("   ")
        assert chunks == []
    
    def test_encode_texts(self):
        """Test encoding multiple texts."""
        encoder = EmbeddingEncoder()
        
        texts = ["测试文本一", "测试文本二", "测试文本三"]
        embeddings = encoder.encode_texts(texts)
        
        assert embeddings.shape[0] == 3
        assert embeddings.shape[1] == 512
        assert embeddings.dtype == np.float32
    
    def test_encode_texts_empty(self):
        """Test encoding empty list."""
        encoder = EmbeddingEncoder()
        
        embeddings = encoder.encode_texts([])
        assert embeddings.shape == (0, 512)
    
    def test_encode_query(self):
        """Test encoding a single query."""
        encoder = EmbeddingEncoder()
        
        embedding = encoder.encode_query("测试查询")
        
        assert embedding.shape[0] == 1
        assert embedding.shape[1] == 512
    
    def test_encode_query_empty(self):
        """Test encoding empty query."""
        encoder = EmbeddingEncoder()
        
        embedding = encoder.encode_query("")
        assert embedding.shape == (1, 512)
        assert np.allclose(embedding, 0)
    
    def test_encode_documents(self):
        """Test encoding documents with chunking."""
        encoder = EmbeddingEncoder(chunk_size=100)
        
        documents = [
            {'content': '这是第一个文档的内容，包含一些测试文本。', 'metadata': {'id': 1}},
            {'content': '这是第二个文档的内容，也包含一些测试文本。', 'metadata': {'id': 2}}
        ]
        
        embeddings, metadata = encoder.encode_documents(documents)
        
        assert embeddings.shape[1] == 512
        assert len(metadata) == embeddings.shape[0]
    
    def test_get_dimension(self):
        """Test getting embedding dimension."""
        encoder = EmbeddingEncoder()
        
        assert encoder.get_dimension() == 512


class TestModelManagement:
    """Test cases for model management."""
    
    def test_get_embedding_model(self):
        """Test model loading."""
        model = get_embedding_model()
        
        assert model is not None
        assert model.get_sentence_embedding_dimension() == 512
    
    def test_model_caching(self):
        """Test that model is cached."""
        model1 = get_embedding_model()
        model2 = get_embedding_model()
        
        assert model1 is model2
    
    def test_clear_cache(self):
        """Test clearing model cache."""
        get_embedding_model()
        clear_model_cache()
        
        # This is a simple test - in practice, you'd check that memory is freed


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
