"""
Embeddings module for semantic indexing.

Provides text encoding and model management capabilities.
"""

from .encoder import EmbeddingEncoder
from .models import get_embedding_model

__all__ = ['EmbeddingEncoder', 'get_embedding_model']
