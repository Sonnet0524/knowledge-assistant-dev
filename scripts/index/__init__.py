"""
Index module for vector storage and management.

Provides FAISS-based vector store and index management.
"""

from .vector_store import VectorStore
from .manager import IndexManager

__all__ = ['VectorStore', 'IndexManager']
