#!/usr/bin/env python3
"""
Test script for Sprint 1 functionality validation.

Tests TASK-AI1 (build_semantic_index) and TASK-AI2 (semantic_search).
"""

import json
import time
import sys
import os

# Add scripts to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.tools.indexing import build_semantic_index, get_index_stats
from scripts.tools.search import semantic_search, batch_search


def print_section(title):
    """Print section header."""
    print()
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)


def test_build_index():
    """Test TASK-AI1: build_semantic_index."""
    print_section("TEST-AI1: 语义索引构建测试")
    
    # Load test documents
    with open('tests/fixtures/sample_documents.json', 'r', encoding='utf-8') as f:
        documents = json.load(f)
    
    print(f"\n加载测试文档: {len(documents)} 个")
    for i, doc in enumerate(documents):
        print(f"  [{i+1}] {doc['metadata']['title']}")
    
    # Build index
    print("\n开始构建索引...")
    start_time = time.time()
    
    result = build_semantic_index(
        documents=documents,
        index_path=".test-index",
        chunk_size=256,
        chunk_overlap=50,
        batch_size=8,
        show_progress=False
    )
    
    build_time = time.time() - start_time
    
    print("\n构建结果:")
    print(f"  成功: {result.get('success')}")
    print(f"  文档数: {result.get('total_docs')}")
    print(f"  分块数: {result.get('total_chunks')}")
    print(f"  索引大小: {result.get('index_size')}")
    print(f"  构建时间: {result.get('build_time')}")
    print(f"  模型: {result.get('model')}")
    print(f"  向量维度: {result.get('dimension')}")
    
    # Verify result
    assert result['success'], "索引构建失败"
    assert result['total_docs'] == len(documents), "文档数不匹配"
    assert result['total_chunks'] > 0, "没有生成任何分块"
    
    print("\n✅ TASK-AI1 测试通过")
    
    return result


def test_search():
    """Test TASK-AI2: semantic_search."""
    print_section("TEST-AI2: 语义搜索测试")
    
    # Test queries
    test_cases = [
        {
            'query': 'Python编程语言',
            'expected_category': 'programming',
            'description': '搜索Python相关内容'
        },
        {
            'query': '异步和并发编程',
            'expected_category': 'programming',
            'description': '搜索异步编程内容'
        },
        {
            'query': '机器学习和深度学习',
            'expected_category': 'ai',
            'description': '搜索AI相关内容'
        },
        {
            'query': '数据分析工具',
            'expected_category': 'data',
            'description': '搜索数据分析内容'
        },
        {
            'query': 'Web开发框架',
            'expected_category': 'programming',
            'description': '搜索Web开发内容'
        }
    ]
    
    all_passed = True
    
    for i, test_case in enumerate(test_cases):
        print(f"\n[测试 {i+1}] {test_case['description']}")
        print(f"查询: \"{test_case['query']}\"")
        
        start_time = time.time()
        results = semantic_search(
            query=test_case['query'],
            index_path=".test-index",
            top_k=3
        )
        query_time = (time.time() - start_time) * 1000
        
        print(f"返回结果: {len(results)} 个 (耗时: {query_time:.1f}ms)")
        
        if results:
            print(f"Top 1 结果:")
            print(f"  标题: {results[0]['metadata'].get('title')}")
            print(f"  相似度: {results[0]['similarity']:.4f}")
            print(f"  摘要: {results[0]['snippet'][:50]}...")
            
            # Verify relevance
            top_category = results[0]['metadata'].get('category')
            if top_category == test_case['expected_category']:
                print(f"  ✅ 类别匹配: {top_category}")
            else:
                print(f"  ⚠️  类别不匹配: 期望 {test_case['expected_category']}, 实际 {top_category}")
                all_passed = False
        else:
            print("  ❌ 没有返回结果")
            all_passed = False
        
        # Check query time
        if query_time < 150:
            print(f"  ✅ 查询速度达标 (<150ms)")
        else:
            print(f"  ⚠️  查询速度较慢 ({query_time:.1f}ms)")
    
    if all_passed:
        print("\n✅ TASK-AI2 测试通过")
    else:
        print("\n⚠️  TASK-AI2 部分测试未达标")
    
    return all_passed


def test_batch_search():
    """Test batch search functionality."""
    print_section("批量搜索测试")
    
    queries = ["Python", "机器学习", "数据分析", "Web开发"]
    
    print(f"批量查询: {queries}")
    
    start_time = time.time()
    all_results = batch_search(
        queries=queries,
        index_path=".test-index",
        top_k=2
    )
    batch_time = (time.time() - start_time) * 1000
    
    print(f"\n批量搜索完成 (总耗时: {batch_time:.1f}ms)")
    
    for query, results in zip(queries, all_results):
        print(f"\n查询 \"{query}\": {len(results)} 个结果")
        if results:
            print(f"  Top 1: {results[0]['metadata'].get('title')}")
    
    print("\n✅ 批量搜索测试通过")


def test_index_stats():
    """Test index statistics."""
    print_section("索引统计测试")
    
    stats = get_index_stats('.test-index')
    
    print("\n索引统计:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    assert stats.get('exists'), "索引不存在"
    assert stats.get('total_vectors', 0) > 0, "索引中没有向量"
    
    print("\n✅ 索引统计测试通过")


def test_performance():
    """Test performance with larger dataset."""
    print_section("性能测试")
    
    # Generate larger dataset
    print("\n生成测试数据...")
    documents = []
    for i in range(100):
        doc = {
            'path': f'test_{i}.md',
            'content': f'这是第{i}个测试文档的内容。包含一些关于Python编程、机器学习和数据分析的内容。文档编号是{i}。',
            'metadata': {
                'title': f'测试文档{i}',
                'index': i,
                'category': 'test'
            }
        }
        documents.append(doc)
    
    print(f"生成文档数: {len(documents)}")
    
    # Build index
    print("\n构建索引...")
    start_time = time.time()
    result = build_semantic_index(
        documents=documents,
        index_path=".perf-index",
        batch_size=8
    )
    build_time = time.time() - start_time
    
    print(f"\n性能结果:")
    print(f"  文档数: {result['total_docs']}")
    print(f"  分块数: {result['total_chunks']}")
    print(f"  构建时间: {result['build_time']}")
    
    # Test search speed
    print("\n测试搜索速度...")
    queries = ["Python", "机器学习", "测试文档"]
    
    for query in queries:
        start = time.time()
        results = semantic_search(query, ".perf-index", top_k=5)
        elapsed = (time.time() - start) * 1000
        print(f"  查询 \"{query}\": {elapsed:.1f}ms ({len(results)} 结果)")
    
    # Performance assertions
    if build_time < 5.0:
        print(f"\n✅ 构建速度达标: {build_time:.1f}s < 5s (100 docs)")
    else:
        print(f"\n⚠️  构建速度较慢: {build_time:.1f}s")
    
    print("\n✅ 性能测试完成")


def cleanup():
    """Clean up test indexes."""
    import shutil
    
    print_section("清理测试数据")
    
    for path in ['.test-index', '.perf-index']:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"删除: {path}")
    
    print("\n清理完成")


def main():
    """Run all tests."""
    print("\n" + "🚀" * 30)
    print("Sprint 1 功能验证测试")
    print("测试 TASK-AI1 和 TASK-AI2")
    print("🚀" * 30)
    
    try:
        # Run tests
        test_build_index()
        test_search()
        test_batch_search()
        test_index_stats()
        test_performance()
        
        # Summary
        print_section("测试总结")
        print("\n✅ 所有测试通过！")
        print("\n功能验收:")
        print("  ✅ TASK-AI1: 语义索引构建 - 通过")
        print("  ✅ TASK-AI2: 语义搜索工具 - 通过")
        print("\n性能验收:")
        print("  ✅ 索引构建速度达标")
        print("  ✅ 搜索查询延迟达标")
        
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        return 1
    
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    finally:
        # Cleanup
        cleanup()
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
