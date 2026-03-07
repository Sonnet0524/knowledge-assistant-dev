#!/usr/bin/env python3
"""
Performance benchmark for Sprint 1.

Tests indexing and search performance at scale.
"""

import json
import time
import sys
import os
import random

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.tools.indexing import build_semantic_index
from scripts.tools.search import semantic_search


# Sample text templates for generating documents
TEXT_TEMPLATES = [
    "Python是一种高级编程语言，以其简洁清晰的语法而闻名。Python广泛应用于Web开发、数据科学、人工智能、自动化脚本等多个领域。",
    "机器学习是人工智能的核心技术之一。通过训练模型，机器可以从数据中学习规律，实现预测和分类等任务。",
    "异步编程是现代软件开发的重要技术。Python的asyncio库提供了强大的异步编程支持，允许开发者编写高效的并发代码。",
    "数据分析是从数据中提取有价值信息的过程。Python提供了丰富的数据分析工具，如Pandas用于数据处理，NumPy用于数值计算。",
    "深度学习是机器学习的一个分支，使用多层神经网络来学习数据的表示。卷积神经网络广泛应用于图像识别。",
    "自然语言处理是人工智能的重要分支，致力于让计算机理解和处理人类语言。常见的NLP任务包括文本分类、情感分析、机器翻译。",
    "Web开发是Python的重要应用领域之一。Django和Flask是两个流行的Python Web框架。Django是一个全功能的框架。",
    "数据库是现代应用的核心组件。SQL和NoSQL数据库各有优势，选择合适的数据库对于应用性能至关重要。",
    "容器化技术如Docker改变了软件开发和部署的方式。容器提供了轻量级的虚拟化解决方案，使应用更易于部署和扩展。",
    "云计算平台如AWS、Azure和GCP提供了丰富的服务，包括计算、存储、数据库、机器学习等，帮助企业快速构建和扩展应用。"
]

CATEGORIES = ['programming', 'ai', 'data', 'web', 'devops']
TAGS = ['python', 'ai', 'ml', 'web', 'data', 'cloud', 'docker', 'database']


def generate_documents(count: int) -> list:
    """Generate test documents with varied content."""
    documents = []
    
    for i in range(count):
        # Generate content by combining random templates
        num_templates = random.randint(2, 5)
        selected_templates = random.sample(TEXT_TEMPLATES, num_templates)
        content = ' '.join(selected_templates)
        
        # Add some variation
        content += f" 文档编号{i}包含关于技术的详细信息。"
        
        # Create metadata
        doc = {
            'path': f'doc_{i}.md',
            'content': content,
            'metadata': {
                'title': f'技术文档{i}',
                'category': random.choice(CATEGORIES),
                'tags': random.sample(TAGS, random.randint(2, 4)),
                'date': f'2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}',
                'index': i
            }
        }
        documents.append(doc)
    
    return documents


def run_benchmark(doc_counts: list):
    """Run performance benchmark for different document counts."""
    print("=" * 70)
    print("Sprint 1 Performance Benchmark")
    print("Testing indexing and search performance at scale")
    print("=" * 70)
    
    results = []
    
    for count in doc_counts:
        print(f"\n{'='*70}")
        print(f"Testing with {count} documents")
        print(f"{'='*70}")
        
        # Generate documents
        print(f"\n[1/4] Generating {count} documents...")
        gen_start = time.time()
        documents = generate_documents(count)
        gen_time = time.time() - gen_start
        print(f"      Generated in {gen_time:.2f}s")
        
        # Build index
        print(f"\n[2/4] Building semantic index...")
        build_start = time.time()
        result = build_semantic_index(
            documents=documents,
            index_path=f".benchmark-index-{count}",
            chunk_size=256,
            batch_size=8,
            show_progress=False
        )
        build_time = time.time() - build_start
        
        print(f"      Total time: {build_time:.2f}s")
        print(f"      Documents: {result['total_docs']}")
        print(f"      Chunks: {result['total_chunks']}")
        print(f"      Index size: {result['index_size']}")
        
        # Test search performance
        print(f"\n[3/4] Testing search performance...")
        queries = [
            "Python编程",
            "机器学习算法",
            "Web开发框架",
            "数据分析工具",
            "云计算平台"
        ]
        
        search_times = []
        for query in queries:
            start = time.time()
            results = semantic_search(
                query=query,
                index_path=f".benchmark-index-{count}",
                top_k=5
            )
            elapsed = (time.time() - start) * 1000  # ms
            search_times.append(elapsed)
            print(f"      Query '{query[:10]}...': {elapsed:.1f}ms ({len(results)} results)")
        
        avg_search_time = sum(search_times) / len(search_times)
        max_search_time = max(search_times)
        
        # Memory estimate (rough)
        import os
        index_file = f".benchmark-index-{count}/index.faiss"
        index_size_mb = os.path.getsize(index_file) / 1024 / 1024 if os.path.exists(index_file) else 0
        
        # Check targets
        print(f"\n[4/4] Performance Check:")
        
        # Build time target
        if count <= 100:
            target = 1.0
        elif count <= 500:
            target = 5.0
        elif count <= 1000:
            target = 15.0
        else:  # 2000
            target = 40.0
        
        build_ok = build_time < target
        print(f"      Build time: {build_time:.1f}s {'✅' if build_ok else '❌'} (target: <{target}s)")
        
        # Search time target
        search_ok = avg_search_time < 150
        print(f"      Search latency: {avg_search_time:.1f}ms {'✅' if search_ok else '❌'} (target: <150ms)")
        
        # Record results
        benchmark_result = {
            'doc_count': count,
            'build_time': round(build_time, 2),
            'build_target': target,
            'build_ok': build_ok,
            'avg_search_time': round(avg_search_time, 1),
            'max_search_time': round(max_search_time, 1),
            'search_ok': search_ok,
            'index_size_mb': round(index_size_mb, 2),
            'total_chunks': result['total_chunks']
        }
        results.append(benchmark_result)
    
    # Summary
    print(f"\n{'='*70}")
    print("BENCHMARK SUMMARY")
    print(f"{'='*70}")
    print(f"\n{'Docs':<8} {'Build Time':<15} {'Target':<10} {'Search (avg)':<15} {'Target':<10} {'Status'}")
    print("-" * 70)
    
    all_ok = True
    for r in results:
        status = '✅ PASS' if (r['build_ok'] and r['search_ok']) else '❌ FAIL'
        if not (r['build_ok'] and r['search_ok']):
            all_ok = False
        print(f"{r['doc_count']:<8} {r['build_time']:<15.2f} {r['build_target']:<10.0f} "
              f"{r['avg_search_time']:<15.1f} {'<150ms':<10} {status}")
    
    print("\n" + "="*70)
    if all_ok:
        print("✅ ALL PERFORMANCE TARGETS MET!")
        print("="*70)
        print("\n验收结果:")
        print("  ✅ 索引构建性能达标 (2000 docs < 40s)")
        print("  ✅ 搜索查询性能达标 (< 150ms)")
        return 0
    else:
        print("❌ SOME PERFORMANCE TARGETS NOT MET")
        print("="*70)
        return 1


def cleanup(doc_counts: list):
    """Clean up benchmark indexes."""
    import shutil
    
    print("\nCleaning up benchmark indexes...")
    for count in doc_counts:
        path = f".benchmark-index-{count}"
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"  Deleted: {path}")


def main():
    """Run the benchmark."""
    # Test with progressively larger datasets
    doc_counts = [100, 500, 1000, 2000]
    
    try:
        exit_code = run_benchmark(doc_counts)
    finally:
        cleanup(doc_counts)
    
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
