"""
Tools module for semantic indexing and search.

Provides high-level API functions for building and searching indexes.
"""

from .indexing import build_semantic_index
from .search import semantic_search

__all__ = ['build_semantic_index', 'semantic_search']
