"""
Pytest configuration and shared fixtures.

This module provides common fixtures and configuration for all tests.
"""

import pytest
import json
import os
from pathlib import Path


# Test directories
TEST_DIR = Path(__file__).parent
FIXTURES_DIR = TEST_DIR / "fixtures"


@pytest.fixture
def sample_documents():
    """Load sample test documents.
    
    Returns:
        List[Dict]: List of test documents with path, content, metadata
    """
    with open(FIXTURES_DIR / "sample_documents.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def large_documents():
    """Load large test documents.
    
    Returns:
        List[Dict]: List of larger test documents
    """
    with open(FIXTURES_DIR / "large_documents.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def temp_index_dir(tmp_path):
    """Create a temporary directory for index files.
    
    Args:
        tmp_path: pytest's built-in tmp_path fixture
        
    Returns:
        Path: Path to temporary index directory
    """
    index_dir = tmp_path / ".ka-index"
    index_dir.mkdir()
    return index_dir


@pytest.fixture
def embedding_model():
    """Load the embedding model (lazy loading with caching).
    
    This fixture is designed to work with the model once TASK-AI1 is complete.
    Currently returns None as a placeholder.
    
    Returns:
        SentenceTransformer: The loaded model, or None if not available
    """
    try:
        from sentence_transformers import SentenceTransformer
        # Use global cache to avoid reloading
        if not hasattr(embedding_model, '_cache'):
            embedding_model._cache = {}
        
        if 'bge_small_zh' not in embedding_model._cache:
            embedding_model._cache['bge_small_zh'] = SentenceTransformer(
                'BAAI/bge-small-zh-v1.5'
            )
        
        return embedding_model._cache['bge_small_zh']
    except ImportError:
        pytest.skip("sentence-transformers not installed")
    except Exception as e:
        pytest.skip(f"Failed to load model: {e}")


@pytest.fixture
def sample_query():
    """Provide a sample query for testing.
    
    Returns:
        str: Sample Chinese query
    """
    return "Python编程入门"


@pytest.fixture
def sample_queries():
    """Provide multiple sample queries.
    
    Returns:
        List[str]: List of sample queries
    """
    return [
        "Python编程",
        "异步编程技术",
        "机器学习算法",
        "深度学习神经网络",
        "自然语言处理"
    ]


# pytest configuration
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "performance: mark test as a performance test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


# Skip slow tests by default
def pytest_addoption(parser):
    """Add command line options for pytest."""
    parser.addoption(
        "--run-slow", 
        action="store_true", 
        default=False, 
        help="run slow tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection based on options."""
    if config.getoption("--run-slow"):
        return
    
    skip_slow = pytest.mark.skip(reason="need --run-slow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
