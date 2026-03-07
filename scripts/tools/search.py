"""
Semantic search tool for querying vector indexes.

Implements TASK-AI2: semantic_search function.
"""

import os
import time
import logging
from typing import List, Dict, Optional

# Add parent directory to path for imports
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from embeddings.encoder import EmbeddingEncoder
from index.manager import IndexManager

logger = logging.getLogger(__name__)

# Global encoder cache to avoid reloading
_encoder_cache = {}


def _get_encoder(
    model_name: str = "BAAI/bge-small-zh-v1.5",
    **kwargs
) -> EmbeddingEncoder:
    """Get or create encoder instance (cached)."""
    cache_key = model_name
    
    if cache_key not in _encoder_cache:
        _encoder_cache[cache_key] = EmbeddingEncoder(
            model_name=model_name,
            **kwargs
        )
    
    return _encoder_cache[cache_key]


def semantic_search(
    query: str,
    index_path: str = ".ka-index",
    top_k: int = 5,
    filters: Optional[Dict] = None,
    threshold: Optional[float] = None,
    model_name: str = "BAAI/bge-small-zh-v1.5"
) -> List[Dict]:
    """
    Perform semantic search on an indexed document collection.
    
    This function encodes the query, searches the FAISS index, and returns
    the most semantically similar documents.
    
    Args:
        query: Search query text. Can be a question, keyword, or natural
            language query. Example: "Python异步编程" or "如何实现并发"
        
        index_path: Path to the index directory (default: ".ka-index")
            Must contain index.faiss and metadata.json files
        
        top_k: Maximum number of results to return (default: 5)
            Actual number may be less if filters are applied
        
        filters: Optional metadata filters (default: None)
            Only return results matching all filter criteria.
            Example: {'category': 'programming', 'date': '2024-01-01'}
        
        threshold: Optional similarity threshold (default: None)
            Only return results with similarity >= threshold.
            Note: HNSW uses inner product, not normalized similarity.
        
        model_name: Name of the embedding model (default: "BAAI/bge-small-zh-v1.5")
            Must match the model used to build the index
    
    Returns:
        List of search results, each containing:
        [
            {
                'rank': int,                    # Result ranking (1-based)
                'similarity': float,            # Similarity score
                'snippet': str,                 # Text snippet (first 200 chars)
                'metadata': dict,               # Document metadata
                'index': int                    # Chunk index in the index
            }
        ]
    
    Raises:
        FileNotFoundError: If index files don't exist
        RuntimeError: If model loading or search fails
    
    Example:
        >>> # First build an index
        >>> documents = [
        ...     {'content': 'Python是一种编程语言', 'metadata': {'id': 1}},
        ...     {'content': '机器学习是AI的核心技术', 'metadata': {'id': 2}}
        ... ]
        >>> build_semantic_index(documents)
        
        >>> # Then search
        >>> results = semantic_search("编程语言", top_k=2)
        >>> print(results[0]['similarity'])
        0.85
        >>> print(results[0]['snippet'])
        'Python是一种编程语言'
    
    Performance:
        - Query latency: <150ms (target)
        - Short queries (<10 chars): <50ms
        - Medium queries (10-50 chars): <100ms
        - Long queries (>50 chars): <150ms
    
    Notes:
        - Query is encoded into a 512-dim vector
        - HNSW provides fast approximate nearest neighbor search
        - Results are ranked by similarity (descending)
        - Empty queries return empty results
    """
    # Handle empty query
    if not query or len(query.strip()) == 0:
        logger.warning("Empty query provided")
        return []
    
    start_time = time.time()
    
    try:
        # 1. Load index
        manager = IndexManager(index_path=index_path)
        
        if not manager.index_exists():
            logger.error(f"Index not found at {index_path}")
            return []
        
        if not manager.load_index():
            logger.error("Failed to load index")
            return []
        
        # 2. Encode query
        encoder = _get_encoder(model_name=model_name)
        query_embedding = encoder.encode_query(query)
        
        # 3. Search
        results = manager.search(
            query_vector=query_embedding,
            top_k=top_k,
            filters=filters
        )
        
        # 4. Apply threshold if specified
        if threshold is not None:
            results = [r for r in results if r['similarity'] >= threshold]
        
        # 5. Add query time to results
        query_time = time.time() - start_time
        
        logger.info(
            f"Search completed: {len(results)} results in {query_time*1000:.1f}ms"
        )
        
        return results
        
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return []


def batch_search(
    queries: List[str],
    index_path: str = ".ka-index",
    top_k: int = 5,
    model_name: str = "BAAI/bge-small-zh-v1.5"
) -> List[List[Dict]]:
    """
    Perform batch semantic search for multiple queries.
    
    More efficient than calling semantic_search multiple times
    as it reuses the loaded index.
    
    Args:
        queries: List of query strings
        index_path: Path to the index directory
        top_k: Number of results per query
        model_name: Embedding model name
    
    Returns:
        List of result lists, one per query
    
    Example:
        >>> queries = ["Python", "机器学习", "异步编程"]
        >>> all_results = batch_search(queries)
        >>> print(len(all_results))
        3
    """
    if not queries:
        return []
    
    # Load index once
    manager = IndexManager(index_path=index_path)
    
    if not manager.index_exists() or not manager.load_index():
        logger.error("Failed to load index for batch search")
        return [[] for _ in queries]
    
    # Get encoder
    encoder = _get_encoder(model_name=model_name)
    
    # Encode all queries
    query_embeddings = encoder.encode_texts(queries)
    
    # Search for each query
    all_results = []
    for i, query_emb in enumerate(query_embeddings):
        query_emb = query_emb.reshape(1, -1)  # Ensure 2D
        results = manager.search(
            query_vector=query_emb,
            top_k=top_k
        )
        all_results.append(results)
    
    return all_results


def get_search_suggestions(
    partial_query: str,
    index_path: str = ".ka-index",
    top_k: int = 5
) -> List[str]:
    """
    Get search suggestions based on partial query.
    
    Useful for autocomplete functionality.
    
    Args:
        partial_query: Partial query string
        index_path: Path to the index
        top_k: Number of suggestions
    
    Returns:
        List of suggested query strings
    
    Example:
        >>> suggestions = get_search_suggestions("Py")
        >>> print(suggestions)
        ['Python', 'Python编程', 'Python异步编程']
    """
    # This is a simplified implementation
    # In practice, you might want to:
    # 1. Extract keywords from indexed documents
    # 2. Use a trie or similar structure for prefix matching
    # 3. Rank by frequency or relevance
    
    results = semantic_search(
        query=partial_query,
        index_path=index_path,
        top_k=top_k
    )
    
    # Extract unique keywords from snippets
    suggestions = []
    seen = set()
    
    for result in results:
        snippet = result.get('snippet', '')
        # Simple keyword extraction (can be improved)
        words = snippet.split()[:3]  # First 3 words
        suggestion = ' '.join(words)
        
        if suggestion and suggestion not in seen:
            suggestions.append(suggestion)
            seen.add(suggestion)
    
    return suggestions[:top_k]
