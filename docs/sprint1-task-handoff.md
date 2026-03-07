# Sprint 1 任务传达清单

**日期**: 2026-03-07  
**Sprint**: Sprint 1 (Week 1-2)  
**状态**: 准备启动

---

## 📋 任务分配总览

| Team | 任务 | Issue | 优先级 | 工时 | 依赖 |
|------|------|-------|--------|------|------|
| **AI Team** | TASK-AI1: 语义索引构建 | #4 | P0 | 5天 | 无 |
| **AI Team** | TASK-AI2: 语义搜索工具 | #5 | P0 | 3天 | TASK-AI1 |
| **Test Team** | TASK-TE1: 索引构建测试 | #6 | P0 | 2天 | TASK-AI1 |
| **Test Team** | TASK-TE2: 搜索测试 | #7 | P0 | 2天 | TASK-AI2 |

---

## 🤖 给 AI Team 的传达信息

### 📢 Sprint 1 已正式启动！

#### 🎯 核心任务

**任务一：TASK-AI1 - 语义索引构建**
- **Issue**: #4
- **GitHub**: https://github.com/Sonnet0524/SG-AgentTeam/issues/4
- **工时**: 5 天
- **优先级**: P0（最高）

**任务二：TASK-AI2 - 语义搜索工具**
- **Issue**: #5
- **GitHub**: https://github.com/Sonnet0524/SG-AgentTeam/issues/5
- **工时**: 3 天
- **优先级**: P0（最高）

---

### 🔧 技术方案（已确定）

#### 嵌入模型
```
模型：BAAI/bge-small-zh-v1.5
参数：33M
维度：512
模型大小：~130MB
内存占用：~200MB
CPU推理速度：~10ms/句
```

#### 索引策略
```
类型：FAISS HNSW
维度：512
连接数：32
索引大小：~15MB (2000 docs)
```

#### 文档规模
```
数量：~2000 个文档
语言：纯中文
构建时间目标：<40秒（低CPU）
```

---

### ⚙️ 环境准备

#### 第一步：安装依赖

```bash
# 核心依赖
pip install sentence-transformers
pip install faiss-cpu

# 测试工具
pip install pytest pytest-cov

# 可选：日志
pip install loguru
```

#### 第二步：测试模型加载

```bash
# 运行测试
python -c "
from sentence_transformers import SentenceTransformer
import faiss

# 测试模型加载
model = SentenceTransformer('BAAI/bge-small-zh-v1.5')
print('✅ 模型加载成功')
print(f'模型维度: {model.get_sentence_embedding_dimension()}')

# 测试向量编码
embedding = model.encode(['测试文本'])
print(f'✅ 向量维度: {embedding.shape[1]}')

# 测试FAISS
index = faiss.IndexHNSWFlat(512, 32)
print('✅ FAISS索引创建成功')
"
```

#### 第三步：检查工作目录

```bash
# 确认在 dev 仓库
ls practice/agents/ai/
# 应该看到 AGENTS.md 和 CATCH_UP.md

# 查看任务分配文档
cat practice/status/task-assignments/v1.1-task-assignments.md
```

---

### 📂 文件结构规划

```
scripts/
├── embeddings/
│   ├── __init__.py
│   ├── encoder.py              # 向量编码器
│   └── models.py               # 模型管理
├── index/
│   ├── __init__.py
│   ├── vector_store.py         # FAISS向量存储
│   └── manager.py              # 索引管理器
└── tools/
    ├── __init__.py
    ├── indexing.py             # build_semantic_index()
    └── search.py               # semantic_search()
```

---

### 💻 代码实现示例

#### TASK-AI1: 语义索引构建

```python
# scripts/tools/indexing.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from typing import List, Dict

# 全局模型缓存
_model_cache = {}

def get_embedding_model():
    """获取嵌入模型（延迟加载）"""
    if 'bge_small_zh' not in _model_cache:
        _model_cache['bge_small_zh'] = SentenceTransformer(
            'BAAI/bge-small-zh-v1.5'
        )
    return _model_cache['bge_small_zh']

def build_semantic_index(
    documents: List[Dict],
    index_path: str = ".ka-index",
    chunk_size: int = 256,
    chunk_overlap: int = 50,
    batch_size: int = 8
) -> Dict:
    """
    构建语义索引
    
    Args:
        documents: 文档列表 [{'path': ..., 'content': ..., 'metadata': ...}]
        index_path: 索引保存路径
        chunk_size: 分块大小
        chunk_overlap: 分块重叠
        batch_size: 批处理大小
    
    Returns:
        {
            'success': True,
            'total_docs': int,
            'total_chunks': int,
            'index_size': str,
            'build_time': str,
            'model': 'bge-small-zh-v1.5'
        }
    """
    import time
    import os
    
    start_time = time.time()
    
    # 1. 加载模型
    model = get_embedding_model()
    
    # 2. 分块处理
    chunks = []
    chunk_metadata = []
    
    for doc in documents:
        text = doc['content']
        # 简单分块（需要优化）
        for i in range(0, len(text), chunk_size - chunk_overlap):
            chunk = text[i:i + chunk_size]
            if len(chunk) > 0:
                chunks.append(chunk)
                chunk_metadata.append(doc['metadata'])
    
    # 3. 批量编码
    all_embeddings = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        embeddings = model.encode(batch)
        all_embeddings.append(embeddings)
    
    embeddings_matrix = np.vstack(all_embeddings)
    
    # 4. 构建索引
    dimension = embeddings_matrix.shape[1]  # 512
    index = faiss.IndexHNSWFlat(dimension, 32)
    index.add(embeddings_matrix.astype('float32'))
    
    # 5. 保存索引
    os.makedirs(index_path, exist_ok=True)
    faiss.write_index(index, f"{index_path}/index.faiss")
    
    # 6. 保存元数据
    import json
    with open(f"{index_path}/metadata.json", 'w', encoding='utf-8') as f:
        json.dump({
            'chunks': chunks,
            'metadata': chunk_metadata
        }, f, ensure_ascii=False, indent=2)
    
    build_time = time.time() - start_time
    
    return {
        'success': True,
        'total_docs': len(documents),
        'total_chunks': len(chunks),
        'index_size': f"{os.path.getsize(f'{index_path}/index.faiss') / 1024 / 1024:.2f} MB",
        'build_time': f"{build_time:.1f}s",
        'model': 'bge-small-zh-v1.5'
    }
```

#### TASK-AI2: 语义搜索工具

```python
# scripts/tools/search.py

from sentence_transformers import SentenceTransformer
import faiss
import json
from typing import List, Dict

def semantic_search(
    query: str,
    index_path: str = ".ka-index",
    top_k: int = 5,
    filters: Dict = None
) -> List[Dict]:
    """
    语义搜索
    
    Args:
        query: 查询文本
        index_path: 索引路径
        top_k: 返回结果数量
        filters: 元数据过滤条件（可选）
    
    Returns:
        [
            {
                'path': str,
                'similarity': float,
                'snippet': str,
                'metadata': dict
            }
        ]
    """
    # 1. 加载模型
    from .indexing import get_embedding_model
    model = get_embedding_model()
    
    # 2. 加载索引
    index = faiss.read_index(f"{index_path}/index.faiss")
    
    # 3. 加载元数据
    with open(f"{index_path}/metadata.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
        chunks = data['chunks']
        metadata = data['metadata']
    
    # 4. 编码查询
    query_embedding = model.encode([query])
    
    # 5. 搜索
    distances, indices = index.search(query_embedding.astype('float32'), top_k)
    
    # 6. 构建结果
    results = []
    for idx, distance in zip(indices[0], distances[0]):
        similarity = 1 - distance  # 转换为相似度
        results.append({
            'path': metadata[idx].get('path', ''),
            'similarity': float(similarity),
            'snippet': chunks[idx][:200],  # 截取前200字符
            'metadata': metadata[idx]
        })
    
    # 7. 应用过滤器（如果有）
    if filters:
        results = [r for r in results if 
                   all(r['metadata'].get(k) == v for k, v in filters.items())]
    
    return results
```

---

### 📊 性能目标（低CPU环境）

#### 索引构建
| 文档数 | 构建时间 | 内存峰值 | 索引大小 |
|--------|----------|----------|----------|
| 100 | ~1秒 | ~200MB | ~0.8MB |
| 500 | ~5秒 | ~300MB | ~4MB |
| 1000 | ~15秒 | ~400MB | ~8MB |
| **2000** | **<40秒** | **<500MB** | **~15MB** |

#### 搜索查询
| 查询类型 | 延迟 | 准确率 |
|---------|------|--------|
| 短查询（<10字） | <50ms | >85% |
| 中等查询（10-50字） | <100ms | >90% |
| 长查询（>50字） | <150ms | >88% |

---

### 📅 时间安排

| 阶段 | 时间 | 任务 |
|------|------|------|
| **环境准备** | Day 1 | 安装依赖，测试模型 |
| **TASK-AI1 开发** | Day 1-5 | 实现索引构建功能 |
| **TASK-AI2 开发** | Day 6-8 | 实现搜索功能 |
| **测试优化** | Day 9-10 | 性能测试，Bug修复 |

---

### ✅ 验收标准

#### TASK-AI1
- [ ] 函数接受文档列表
- [ ] 使用 bge-small-zh-v1.5 生成向量
- [ ] 构建 FAISS HNSW 索引
- [ ] 保存索引到磁盘
- [ ] 返回结构化结果
- [ ] 单元测试覆盖率 >85%
- [ ] 性能：2000 docs <40秒
- [ ] 内存峰值 <500MB

#### TASK-AI2
- [ ] 从磁盘加载索引
- [ ] 生成查询向量
- [ ] 执行向量搜索
- [ ] 返回排序结果
- [ ] 支持元数据过滤
- [ ] 单元测试覆盖率 >85%
- [ ] 查询延迟 <150ms

---

### 🔔 重要注意事项

#### 模型相关
1. **首次运行**：模型会自动下载（~130MB），需要网络连接
2. **缓存位置**：`~/.cache/huggingface/`
3. **内存管理**：使用全局缓存避免重复加载

#### 性能优化
1. **分块大小**：256字符（适合CPU）
2. **批处理**：8个文档/批次（低内存）
3. **索引类型**：HNSW（平衡速度和质量）

#### 代码规范
1. **类型注解**：所有函数添加类型注解
2. **文档字符串**：详细的函数说明
3. **错误处理**：添加适当的异常处理
4. **日志记录**：记录关键操作和性能指标

#### 提交规范
1. **Commit Message**: 关联 Issue 号（如 `#4`, `#5`）
2. **代码审查**：完成后创建 Pull Request
3. **测试覆盖**：确保 >85% 覆盖率

---

### 📚 参考资源

#### 技术文档
- `docs/technical-design-v1.1.md` - 完整技术设计
- `practice/status/task-assignments/v1.1-task-assignments.md` - 任务分配

#### 模型文档
- [BGE Models](https://huggingface.co/BAAI/bge-small-zh-v1.5)
- [Sentence Transformers](https://www.sbert.net/)

#### 工具文档
- [FAISS Documentation](https://faiss.ai/)

---

### 🚨 遇到问题？

1. **技术问题**：在 GitHub Issue 中留言
2. **环境问题**：检查依赖版本
3. **性能问题**：记录详细日志并反馈

---

## 🧪 给 Test Team 的传达信息

### 📢 Sprint 1 已启动，准备测试工作！

#### 🎯 核心任务

**任务一：TASK-TE1 - 索引构建测试**
- **Issue**: #6
- **GitHub**: https://github.com/Sonnet0524/SG-AgentTeam/issues/6
- **工时**: 2 天
- **依赖**: TASK-AI1 完成

**任务二：TASK-TE2 - 搜索测试**
- **Issue**: #7
- **GitHub**: https://github.com/Sonnet0524/SG-AgentTeam/issues/7
- **工时**: 2 天
- **依赖**: TASK-AI2 完成

---

### 🛠️ 立即可做的准备工作

#### 第一步：安装测试依赖

```bash
# 测试工具
pip install pytest pytest-cov

# 可选：代码质量检查
pip install black flake8 mypy
```

#### 第二步：准备测试数据

创建测试数据目录：
```bash
mkdir -p tests/fixtures
```

创建测试数据文件 `tests/fixtures/sample_documents.json`：
```json
[
  {
    "path": "test1.md",
    "content": "Python是一种高级编程语言，广泛应用于Web开发、数据科学、人工智能等领域。Python的语法简洁清晰，易于学习和使用。",
    "metadata": {
      "title": "Python入门指南",
      "date": "2024-01-01",
      "category": "programming"
    }
  },
  {
    "path": "test2.md",
    "content": "异步编程是现代软件开发的重要技术。Python的asyncio库提供了强大的异步编程支持，可以显著提高程序的并发性能。",
    "metadata": {
      "title": "Python异步编程详解",
      "date": "2024-01-02",
      "category": "programming"
    }
  },
  {
    "path": "test3.md",
    "content": "机器学习是人工智能的核心技术之一。通过训练模型，机器可以从数据中学习规律，实现预测和分类等任务。",
    "metadata": {
      "title": "机器学习基础",
      "date": "2024-01-03",
      "category": "ai"
    }
  }
]
```

#### 第三步：设计测试场景

创建 `tests/test_scenarios.md`：
```markdown
# 测试场景设计

## TASK-TE1: 索引构建测试

### 单元测试
- 测试模型加载
- 测试文本分块
- 测试向量编码
- 测试索引构建

### 集成测试
- 端到端索引构建流程
- 索引持久化和加载
- 错误处理

### 性能测试
- 小数据集（100 docs）
- 中数据集（1000 docs）
- 目标数据集（2000 docs）

## TASK-TE2: 搜索测试

### 基础搜索测试
- 单关键词查询
- 多关键词查询
- 长句查询

### 高级搜索测试
- 元数据过滤
- 不同 top_k 值
- 相似度阈值

### 边缘情况测试
- 空查询
- 无结果查询
- 特殊字符
- 超长查询
```

---

### 📂 测试文件结构

```
tests/
├── __init__.py
├── conftest.py                 # pytest配置和fixtures
├── fixtures/
│   └── sample_documents.json   # 测试数据
├── test_embeddings.py          # 编码器测试
├── test_vector_store.py        # 向量存储测试
├── test_indexing.py            # 索引构建测试
└── test_search.py              # 搜索测试
```

---

### 💻 测试代码示例

#### 索引构建测试

```python
# tests/test_indexing.py

import pytest
import json
from scripts.tools.indexing import build_semantic_index

@pytest.fixture
def sample_documents():
    """加载测试数据"""
    with open('tests/fixtures/sample_documents.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def test_build_semantic_index_basic(sample_documents, tmp_path):
    """测试基本的索引构建"""
    index_path = str(tmp_path / "test_index")
    
    result = build_semantic_index(
        documents=sample_documents,
        index_path=index_path
    )
    
    # 验证返回结果
    assert result['success'] == True
    assert result['total_docs'] == len(sample_documents)
    assert result['total_chunks'] > 0
    assert result['build_time'].endswith('s')
    
    # 验证文件创建
    assert (tmp_path / "test_index" / "index.faiss").exists()
    assert (tmp_path / "test_index" / "metadata.json").exists()

def test_build_semantic_index_performance(sample_documents, tmp_path):
    """测试索引构建性能"""
    import time
    
    index_path = str(tmp_path / "test_index")
    
    start_time = time.time()
    result = build_semantic_index(
        documents=sample_documents,
        index_path=index_path
    )
    build_time = time.time() - start_time
    
    # 对于小数据集，构建时间应该很短
    assert build_time < 5.0  # 5秒以内
```

#### 搜索测试

```python
# tests/test_search.py

import pytest
import json
from scripts.tools.indexing import build_semantic_index
from scripts.tools.search import semantic_search

@pytest.fixture
def built_index(sample_documents, tmp_path):
    """构建测试索引"""
    index_path = str(tmp_path / "test_index")
    build_semantic_index(
        documents=sample_documents,
        index_path=index_path
    )
    return index_path

def test_semantic_search_basic(built_index):
    """测试基本搜索功能"""
    results = semantic_search(
        query="Python编程",
        index_path=built_index,
        top_k=2
    )
    
    # 验证返回结果
    assert len(results) == 2
    assert all('similarity' in r for r in results)
    assert all('snippet' in r for r in results)
    assert all('metadata' in r for r in results)

def test_semantic_search_relevance(built_index):
    """测试搜索相关性"""
    # 搜索Python相关内容
    results = semantic_search(
        query="Python",
        index_path=built_index,
        top_k=5
    )
    
    # 第一个结果应该是Python相关的
    assert 'Python' in results[0]['snippet'] or \
           'Python' in results[0]['metadata'].get('title', '')

def test_semantic_search_edge_cases(built_index):
    """测试边缘情况"""
    # 空查询
    results = semantic_search(
        query="",
        index_path=built_index,
        top_k=5
    )
    # 应该返回结果或抛出异常（根据设计决定）
    
    # 无匹配查询
    results = semantic_search(
        query="这是一段完全不相关的内容xyz123",
        index_path=built_index,
        top_k=5
    )
    # 应该返回空列表或低相似度结果
```

---

### 📊 性能测试基准

```python
# tests/test_performance.py

import pytest
import time
from scripts.tools.indexing import build_semantic_index
from scripts.tools.search import semantic_search

def generate_test_documents(count):
    """生成测试文档"""
    docs = []
    for i in range(count):
        docs.append({
            'path': f'test_{i}.md',
            'content': f'这是第{i}个测试文档的内容。包含一些中文文本用于测试。',
            'metadata': {'title': f'文档{i}', 'index': i}
        })
    return docs

@pytest.mark.performance
def test_indexing_performance_100_docs(tmp_path):
    """测试100文档索引性能"""
    docs = generate_test_documents(100)
    index_path = str(tmp_path / "perf_index")
    
    start = time.time()
    result = build_semantic_index(docs, index_path)
    elapsed = time.time() - start
    
    assert elapsed < 1.0  # < 1秒

@pytest.mark.performance
def test_indexing_performance_1000_docs(tmp_path):
    """测试1000文档索引性能"""
    docs = generate_test_documents(1000)
    index_path = str(tmp_path / "perf_index")
    
    start = time.time()
    result = build_semantic_index(docs, index_path)
    elapsed = time.time() - start
    
    assert elapsed < 15.0  # < 15秒

@pytest.mark.performance
def test_search_performance(built_index):
    """测试搜索性能"""
    queries = ['Python', '异步编程', '机器学习']
    
    for query in queries:
        start = time.time()
        results = semantic_search(query, built_index, top_k=5)
        elapsed = time.time() - start
        
        assert elapsed < 0.15  # < 150ms
```

---

### 📅 时间安排

| 阶段 | 时间 | 任务 |
|------|------|------|
| **准备阶段** | 现在 | 安装依赖，准备测试数据 |
| **等待阶段** | Day 1-8 | 等待AI Team完成开发 |
| **TASK-TE1** | Day 9-10 | 索引构建测试 |
| **TASK-TE2** | Day 11-12 | 搜索测试 |

---

### ✅ 验收标准

#### TASK-TE1: 索引构建测试
- [ ] 创建测试文件
- [ ] 单元测试覆盖率 >85%
- [ ] 集成测试通过
- [ ] 性能测试基准建立
- [ ] 边缘情况测试完成

#### TASK-TE2: 搜索测试
- [ ] 创建测试文件
- [ ] 单元测试覆盖率 >85%
- [ ] 搜索准确率测试
- [ ] 性能测试（延迟 <150ms）
- [ ] 边缘情况测试完成

---

### 🔔 重要注意事项

1. **与AI Team沟通**：提前了解API设计
2. **测试数据**：准备多样化的中文测试数据
3. **性能基准**：记录所有性能指标
4. **问题反馈**：及时在Issue中报告发现的问题

---

## 📞 后续沟通

### 进度更新
- **AI Team**: 在 Issue 中定期更新开发进度
- **Test Team**: 发现问题及时反馈

### 问题解决
- **技术问题**: 在 Issue 中讨论
- **阻塞问题**: 立即通知 PM Team

---

**准备完毕！请按照上述信息向各组传达任务。**
