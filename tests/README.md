# Test Suite

**Sprint**: Sprint 1  
**Team**: Test Team  
**Status**: 🟢 Ready (Waiting for AI Team)

---

## Quick Start

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run with coverage
python3 -m pytest tests/ --cov=scripts --cov-report=html

# Run specific test file
python3 -m pytest tests/test_indexing.py -v

# Run slow tests
python3 -m pytest tests/ --run-slow

# Run only unit tests
python3 -m pytest tests/ -m unit
```

---

## Test Structure

```
tests/
├── __init__.py              # Package init
├── conftest.py              # Pytest configuration & fixtures
├── test_scenarios.md        # Test scenario documentation
├── fixtures/                # Test data
│   ├── sample_documents.json    # Basic test documents (5 docs)
│   └── large_documents.json     # Extended test documents (3 docs)
├── test_embeddings.py       # Encoder tests (TODO)
├── test_vector_store.py     # Vector store tests (TODO)
├── test_indexing.py         # Index building tests (TODO)
└── test_search.py           # Search tests (TODO)
```

---

## Test Fixtures

### sample_documents.json
- **用途**: 基础功能测试
- **规模**: 5 个文档
- **内容**: Python 编程、异步编程、机器学习、深度学习、NLP

### large_documents.json
- **用途**: 扩展功能测试
- **规模**: 3 个文档
- **内容**: 知识管理系统、向量数据库、文本嵌入

---

## Test Categories

### Unit Tests (`@pytest.mark.unit`)
- 模型加载测试
- 文本分块测试
- 向量编码测试
- 索引构建测试

### Integration Tests (`@pytest.mark.integration`)
- 端到端流程测试
- 持久化测试
- 错误处理测试

### Performance Tests (`@pytest.mark.performance`)
- 索引构建性能
- 搜索查询性能
- 内存使用测试

---

## Dependencies

```bash
# Test framework
pytest>=7.0.0
pytest-cov>=4.0.0

# AI dependencies (for testing)
sentence-transformers>=2.0.0
faiss-cpu>=1.7.0
```

---

## Current Status

| Task | Issue | Status | Dependencies |
|------|-------|--------|--------------|
| TASK-TE1: 索引构建测试 | #6 | ⏸️ Waiting | TASK-AI1 (#4) |
| TASK-TE2: 搜索测试 | #7 | ⏸️ Waiting | TASK-AI2 (#5) |

---

## Notes

1. 等待 AI Team 完成 TASK-AI1 和 TASK-AI2
2. 测试文件将在相应功能开发完成后创建
3. 性能测试将在功能稳定后执行

---

## Contact

- **Test Team**: 查看 `practice/agents/test/` 目录
- **Issues**: https://github.com/Sonnet0524/SG-AgentTeam/issues
