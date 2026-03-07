"""
Model management for embedding models.

Provides singleton pattern for model loading and caching.
"""

from sentence_transformers import SentenceTransformer
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Global model cache
_model_cache = {}

# Model configuration
DEFAULT_MODEL = 'BAAI/bge-small-zh-v1.5'
MODEL_DIMENSION = 512


def get_embedding_model(
    model_name: str = DEFAULT_MODEL,
    cache_dir: Optional[str] = None,
    device: str = 'cpu'
) -> SentenceTransformer:
    """
    Get or create an embedding model instance (singleton pattern).
    
    Args:
        model_name: Name or path of the embedding model
        cache_dir: Directory to cache downloaded models
        device: Device to run the model on ('cpu' or 'cuda')
    
    Returns:
        SentenceTransformer model instance
    
    Example:
        >>> model = get_embedding_model()
        >>> embeddings = model.encode(['测试文本'])
        >>> print(embeddings.shape)
        (1, 512)
    """
    cache_key = f"{model_name}_{device}"
    
    if cache_key not in _model_cache:
        logger.info(f"Loading embedding model: {model_name}")
        
        # Create model instance
        model = SentenceTransformer(
            model_name,
            cache_folder=cache_dir,
            device=device
        )
        
        # Verify model dimension
        actual_dim = model.get_sentence_embedding_dimension()
        if actual_dim != MODEL_DIMENSION:
            logger.warning(
                f"Model dimension {actual_dim} differs from expected {MODEL_DIMENSION}"
            )
        
        _model_cache[cache_key] = model
        logger.info(f"Model loaded successfully. Dimension: {actual_dim}")
    
    return _model_cache[cache_key]


def clear_model_cache() -> None:
    """
    Clear the model cache to free memory.
    
    Use this when switching models or freeing resources.
    """
    global _model_cache
    _model_cache.clear()
    logger.info("Model cache cleared")


def get_model_info() -> dict:
    """
    Get information about cached models.
    
    Returns:
        Dictionary with cached model information
    """
    return {
        'cached_models': list(_model_cache.keys()),
        'default_model': DEFAULT_MODEL,
        'model_dimension': MODEL_DIMENSION
    }
