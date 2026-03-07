# Knowledge Assistant - Skill Definition

> 🎯 A semantic knowledge management skill for intelligent document indexing and retrieval

**Version**: v1.1  
**Last Updated**: 2026-03-07  
**Author**: Integration Team  
**Status**: Production Ready

---

## 📖 Overview

**Knowledge Assistant** is a specialized skill that provides semantic indexing, intelligent search, knowledge extraction, and multi-source integration capabilities. It transforms how you interact with your document collections by understanding the semantic meaning of your queries.

### Core Capabilities

- 🔨 **Build Knowledge Base** - Create semantic indexes from document collections
- 🔍 **Semantic Search** - Find documents by meaning, not just keywords
- 📊 **Knowledge Extraction** - Extract keywords and generate summaries
- 📧 **Multi-Source Integration** - Search across documents, emails, and more

### Design Philosophy

```
opencode (Master Agent)
  ├── File operations (built-in)
  ├── Natural language understanding (built-in)
  ├── Intent recognition (built-in)
  └── Calls Knowledge Assistant tools
      ↓
Knowledge Assistant (Tool Library)
  ├── build_semantic_index() → IndexResult
  ├── semantic_search() → [SearchResult]
  ├── extract_keywords() → [Keyword]
  ├── generate_summary() → Summary
  └── EmailConnector → EmailData
```

**Key Principle**: Knowledge Assistant provides algorithms and returns structured data. opencode handles file operations, user interaction, and result presentation.

---

## 🎯 Trigger Patterns

Knowledge Assistant is triggered by natural language phrases indicating knowledge management intents.

### Intent Categories

#### 1. Build Knowledge Base

**Trigger Phrases**:
```
- "build knowledge base from {directory}"
- "create index for {path}"
- "index my documents in {folder}"
- "add {directory} to knowledge base"
- "构建知识库从 {目录}"
- "为 {路径} 创建索引"
```

**Extracted Parameters**:
- `directory`: Path to document collection (required)
- `index_name`: Custom index name (optional, default: ".ka-index")
- `recursive`: Include subdirectories (optional, default: true)

**Example**:
```
User: "build knowledge base from ./notes"
opencode: 
  1. Scans ./notes directory
  2. Reads all document files
  3. Calls build_semantic_index(documents)
  4. Reports: "Indexed 156 documents, created 489 chunks"
```

---

#### 2. Search Documents

**Trigger Phrases**:
```
- "search for {query}"
- "find documents about {topic}"
- "查找关于 {主题} 的文档"
- "搜索 {关键词}"
- "what documents mention {term}"
```

**Extracted Parameters**:
- `query`: Search query text (required)
- `top_k`: Number of results (optional, default: 5)
- `filters`: Metadata filters (optional)
- `threshold`: Similarity threshold (optional)

**Example**:
```
User: "find documents about Python async programming"
opencode:
  1. Recognizes search intent
  2. Calls semantic_search("Python async programming")
  3. Reads top results from disk
  4. Displays: "Found 5 relevant documents..."
```

---

#### 3. Extract Knowledge

**Trigger Phrases**:
```
- "extract keywords from {document}"
- "summarize {document}"
- "what are the key points in {path}"
- "从 {文档} 提取关键词"
- "总结 {文档}"
```

**Extracted Parameters**:
- `document`: Path to document or content (required)
- `method`: Extraction method (optional: "tfidf", "textrank")
- `top_n`: Number of keywords (optional, default: 10)

**Example**:
```
User: "extract keywords from ./notes/python.md"
opencode:
  1. Reads ./notes/python.md
  2. Calls extract_keywords(content)
  3. Displays: "Keywords: Python, async, concurrent, ..."
```

---

#### 4. Multi-Source Search

**Trigger Phrases**:
```
- "search emails for {query}"
- "find in all sources: {query}"
- "search my emails and documents for {topic}"
- "搜索邮件中的 {关键词}"
```

**Extracted Parameters**:
- `query`: Search query (required)
- `sources`: List of sources (optional: ["documents", "emails"])
- `email_folder`: Email folder to search (optional)

**Example**:
```
User: "search emails for project budget"
opencode:
  1. Recognizes email search intent
  2. Connects to EmailConnector
  3. Searches emails
  4. Displays: "Found 3 emails about project budget..."
```

---

## 🛠️ Tool Functions

### 1. build_semantic_index

**Purpose**: Create a semantic vector index from a document collection.

**API**:
```python
from scripts.tools.indexing import build_semantic_index

result = build_semantic_index(
    documents: List[Dict],      # Document list
    index_path: str = ".ka-index",  # Index directory
    chunk_size: int = 256,      # Chunk size in characters
    chunk_overlap: int = 50,    # Overlap between chunks
    batch_size: int = 8,        # Batch size for encoding
    model_name: str = "BAAI/bge-small-zh-v1.5",  # Embedding model
    show_progress: bool = False  # Show progress bar
) -> Dict
```

**Input Format**:
```python
documents = [
    {
        'content': 'Document text content...',
        'metadata': {
            'path': './notes/python.md',
            'title': 'Python Guide',
            'date': '2024-01-15',
            # ... custom metadata
        }
    },
    # ... more documents
]
```

**Output Format**:
```python
{
    'success': True,
    'total_docs': 156,
    'total_chunks': 489,
    'index_size': '23.5 MB',
    'build_time': '12.3s',
    'model': 'BAAI/bge-small-zh-v1.5',
    'dimension': 512,
    'index_path': '.ka-index'
}
```

**opencode Usage**:
```python
# opencode provides documents (scans files)
documents = []  # opencode fills this
for file_path in scan_directory("./notes"):
    content = read_file(file_path)
    documents.append({
        'content': content,
        'metadata': {'path': file_path}
    })

# opencode calls knowledge-assistant tool
result = build_semantic_index(documents)

# opencode presents results
print(f"Indexed {result['total_docs']} documents")
```

**Performance**:
- 100 docs: ~1s
- 1000 docs: ~15s
- 2000 docs: <40s (target)

---

### 2. semantic_search

**Purpose**: Perform semantic search on an indexed collection.

**API**:
```python
from scripts.tools.search import semantic_search

results = semantic_search(
    query: str,                 # Search query
    index_path: str = ".ka-index",  # Index directory
    top_k: int = 5,             # Max results
    filters: Optional[Dict] = None,  # Metadata filters
    threshold: Optional[float] = None,  # Similarity threshold
    model_name: str = "BAAI/bge-small-zh-v1.5"  # Model name
) -> List[Dict]
```

**Input Format**:
```python
# Natural language query
query = "Python异步编程最佳实践"

# Optional filters
filters = {
    'category': 'programming',
    'date_from': '2024-01-01'
}
```

**Output Format**:
```python
[
    {
        'rank': 1,
        'similarity': 0.89,
        'snippet': 'Python async programming allows...',
        'metadata': {
            'path': './notes/python.md',
            'title': 'Python Guide',
            # ... other metadata
        },
        'index': 42  # Chunk index
    },
    # ... more results
]
```

**opencode Usage**:
```python
# opencode understands user intent
query = "Python异步编程"

# opencode calls knowledge-assistant tool
results = semantic_search(query, top_k=5)

# opencode reads and displays documents
for result in results:
    doc_path = result['metadata']['path']
    content = read_file(doc_path)
    display_result(
        title=result['metadata']['title'],
        snippet=result['snippet'],
        similarity=result['similarity'],
        full_content=content
    )
```

**Performance**:
- Query latency: <150ms
- Accuracy: >85% for relevant queries

---

### 3. extract_keywords

**Purpose**: Extract keywords from text content.

**API**:
```python
from scripts.tools.extraction import extract_keywords

keywords = extract_keywords(
    content: str,               # Text content
    method: str = "tfidf",      # Method: "tfidf" or "textrank"
    top_n: int = 10             # Number of keywords
) -> List[Dict]
```

**Output Format**:
```python
[
    {
        'keyword': 'Python',
        'score': 0.85,
        'frequency': 15
    },
    {
        'keyword': '异步编程',
        'score': 0.78,
        'frequency': 12
    },
    # ... more keywords
]
```

**opencode Usage**:
```python
# opencode reads document
content = read_file("./notes/python.md")

# opencode calls knowledge-assistant tool
keywords = extract_keywords(content, method="textrank")

# opencode displays keywords
for kw in keywords:
    print(f"- {kw['keyword']} (score: {kw['score']:.2f})")
```

---

### 4. generate_summary

**Purpose**: Generate a summary from text content.

**API**:
```python
from scripts.tools.extraction import generate_summary

summary = generate_summary(
    content: str,               # Text content
    max_length: int = 200,      # Max characters
    method: str = "extractive"  # Method: "extractive"
) -> Dict
```

**Output Format**:
```python
{
    'summary': 'Python是一种广泛使用的编程语言，支持异步编程...',
    'length': 150,
    'compression_ratio': 0.15,  # Original length / summary length
    'key_sentences': [
        'Python是一种广泛使用的编程语言',
        '支持异步编程特性',
        # ...
    ]
}
```

**opencode Usage**:
```python
# opencode reads document
content = read_file("./notes/python.md")

# opencode calls knowledge-assistant tool
result = generate_summary(content, max_length=200)

# opencode displays summary
print(f"Summary: {result['summary']}")
```

---

### 5. EmailConnector

**Purpose**: Connect to email servers and search emails.

**API**:
```python
from scripts.connectors.email import EmailConnector, EmailConfig

# Configure connection
config = EmailConfig(
    server="imap.gmail.com",
    port=993,
    username="user@gmail.com",
    password="app_password",
    use_ssl=True
)

# Create connector
connector = EmailConnector(config=config)

# Connect
if connector.connect():
    # Search emails
    results = connector.search(
        query="project budget",
        limit=10,
        folders=["INBOX"],
        filters={
            'date_from': '2024-01-01',
            'unread_only': False
        }
    )
    
    # Get full email
    email = connector.get_by_id("msg_123")
    
    # Disconnect
    connector.disconnect()
```

**Search Output Format**:
```python
[
    {
        'id': '123',
        'title': 'Budget Report Q1',
        'snippet': 'Please find attached the Q1 budget...',
        'source': 'email',
        'metadata': {
            'sender': 'boss@company.com',
            'sender_name': 'John Doe',
            'folder': 'INBOX',
            'is_read': True,
            'has_attachments': True,
            'flags': ['seen']
        },
        'timestamp': datetime(2024, 1, 15, 10, 30)
    },
    # ... more results
]
```

**opencode Usage**:
```python
# opencode recognizes email search intent
query = "project budget"

# opencode uses EmailConnector
config = EmailConfig(
    server=get_config('email.server'),
    username=get_config('email.username'),
    password=get_config('email.password')
)

with EmailConnector(config) as connector:
    results = connector.search(query)
    
    # opencode displays results
    for result in results:
        display_email_result(
            subject=result['title'],
            sender=result['metadata']['sender'],
            date=result['timestamp'],
            snippet=result['snippet']
        )
```

---

## 📋 Complete Usage Examples

### Example 1: Build and Search Knowledge Base

**User Request**:
```
"Build a knowledge base from my notes folder and search for Python async programming"
```

**opencode Workflow**:
```python
# Step 1: Scan directory
documents = []
for file_path in scan_directory("./notes", recursive=True):
    if file_path.endswith(('.md', '.txt', '.pdf')):
        content = read_file(file_path)
        metadata = extract_metadata(file_path)
        documents.append({
            'content': content,
            'metadata': metadata
        })

# Step 2: Build index
result = build_semantic_index(documents)
print(f"✓ Indexed {result['total_docs']} documents")
print(f"✓ Created {result['total_chunks']} chunks in {result['build_time']}")

# Step 3: Search
results = semantic_search("Python async programming", top_k=5)

# Step 4: Display results
for i, result in enumerate(results, 1):
    print(f"\n{i}. {result['metadata']['title']}")
    print(f"   Similarity: {result['similarity']:.2f}")
    print(f"   Path: {result['metadata']['path']}")
    print(f"   Snippet: {result['snippet'][:100]}...")
```

**Output**:
```
✓ Indexed 156 documents
✓ Created 489 chunks in 12.3s

Found 5 relevant documents:

1. Python异步编程指南
   Similarity: 0.89
   Path: ./notes/python/async.md
   Snippet: Python async programming allows you to write concurrent code using the async/await syntax...

2. 并发编程最佳实践
   Similarity: 0.85
   Path: ./notes/python/concurrency.md
   Snippet: When working with async programming in Python, consider the following best practices...
...
```

---

### Example 2: Extract Knowledge from Document

**User Request**:
```
"Extract keywords and summarize the document at ./notes/python.md"
```

**opencode Workflow**:
```python
# Step 1: Read document
content = read_file("./notes/python.md")

# Step 2: Extract keywords
keywords = extract_keywords(content, method="textrank", top_n=10)

# Step 3: Generate summary
summary = generate_summary(content, max_length=200)

# Step 4: Display results
print("📄 Document: python.md\n")
print("🔑 Keywords:")
for kw in keywords[:5]:
    print(f"  - {kw['keyword']} (score: {kw['score']:.2f})")

print("\n📝 Summary:")
print(summary['summary'])
print(f"\nCompression ratio: {summary['compression_ratio']:.2f}")
```

**Output**:
```
📄 Document: python.md

🔑 Keywords:
  - Python (score: 0.89)
  - 异步编程 (score: 0.85)
  - 并发 (score: 0.78)
  - async/await (score: 0.75)
  - 性能优化 (score: 0.72)

📝 Summary:
Python是一种广泛使用的编程语言，支持异步编程特性。通过async/await语法，可以编写高效的并发代码。异步编程适用于I/O密集型任务，能显著提升程序性能。

Compression ratio: 0.15
```

---

### Example 3: Multi-Source Search

**User Request**:
```
"Search for 'budget meeting' in my emails and documents"
```

**opencode Workflow**:
```python
# Step 1: Search documents
doc_results = semantic_search("budget meeting", top_k=3)

# Step 2: Search emails
email_config = EmailConfig(
    server=get_config('email.server'),
    username=get_config('email.username'),
    password=get_config('email.password')
)

email_results = []
with EmailConnector(email_config) as connector:
    email_results = connector.search("budget meeting", limit=3)

# Step 3: Merge and rank results
all_results = merge_results(doc_results, email_results)

# Step 4: Display unified results
print(f"Found {len(all_results)} results:\n")

for i, result in enumerate(all_results, 1):
    if result['source'] == 'document':
        print(f"{i}. [Document] {result['metadata']['title']}")
        print(f"   Path: {result['metadata']['path']}")
    else:
        print(f"{i}. [Email] {result['title']}")
        print(f"   From: {result['metadata']['sender']}")
    print(f"   Snippet: {result['snippet'][:80]}...\n")
```

**Output**:
```
Found 6 results:

1. [Email] Budget Meeting Notes - Q1 Review
   From: boss@company.com
   Snippet: Attached are the notes from today's budget meeting. We discussed...

2. [Document] Budget Planning 2024
   Path: ./notes/budget/planning.md
   Snippet: Budget meeting scheduled for next week. Key topics include...

3. [Email] Re: Budget Meeting Tomorrow
   From: colleague@company.com
   Snippet: I'll prepare the budget meeting materials as discussed...
...
```

---

## 🔧 Error Handling

### Common Errors and Solutions

#### 1. Index Not Found

**Error**:
```
FileNotFoundError: Index not found at .ka-index
```

**opencode Response**:
```
"I couldn't find a knowledge base index. Would you like me to build one? 
Just tell me which directory to index, for example: 
'Build knowledge base from ./notes'"
```

#### 2. Email Not Configured

**Error**:
```
ValueError: Email server configuration missing
```

**opencode Response**:
```
"Email search requires configuration. Would you like to set up email access?
I'll need:
- IMAP server (e.g., imap.gmail.com)
- Email address
- Password or app password

You can provide these securely, or skip email search for now."
```

#### 3. Model Loading Failed

**Error**:
```
RuntimeError: Failed to load embedding model
```

**opencode Response**:
```
"The embedding model couldn't be loaded. This might be the first time 
using Knowledge Assistant. The model will be downloaded automatically 
(~130MB). Please ensure you have internet connection and try again."
```

---

## 🎓 Best Practices

### For opencode Users

1. **Build Index Before Searching**
   ```
   # Good
   User: "Build index from ./notes"
   User: "Search for Python async"
   
   # Bad
   User: "Search for Python async"  # No index exists
   ```

2. **Use Natural Language**
   ```
   # Good
   "Find documents about machine learning"
   "What do I have about Python async programming?"
   
   # Also good
   "搜索关于机器学习的文档"
   
   # Less natural
   "semantic_search machine learning"  # Too technical
   ```

3. **Provide Context**
   ```
   # Good
   "Search my notes folder for Python async programming"
   
   # Less specific
   "Search for Python"  # Might return too many results
   ```

4. **Use Filters When Appropriate**
   ```
   "Find documents about budget from January 2024"
   "Search unread emails for project updates"
   ```

### For Developers

1. **Separation of Concerns**
   - Knowledge Assistant: Provides algorithms and returns structured data
   - opencode: Handles file I/O, user interaction, presentation

2. **Structured Data Exchange**
   ```python
   # Good - structured data
   result = build_semantic_index(documents)
   return {
       'success': True,
       'total_docs': 156,
       'total_chunks': 489
   }
   
   # Bad - mixed concerns
   result = build_semantic_index(documents)
   print(f"Indexed {result['total_docs']} documents")  # Don't print!
   return result
   ```

3. **Error Propagation**
   ```python
   # Good - let opencode handle errors
   try:
       result = semantic_search(query)
       return result
   except FileNotFoundError:
       raise  # Let opencode catch and explain to user
   
   # Bad - handle errors internally
   try:
       result = semantic_search(query)
   except FileNotFoundError:
       print("Index not found")  # Don't handle presentation!
       return None
   ```

---

## 🔮 Future Enhancements

### Planned Features (v1.2+)

- **Incremental Indexing**: Update index without rebuilding
- **Multi-Modal Support**: Images, PDFs, code files
- **Federated Search**: Search across multiple knowledge bases
- **Caching Layer**: Faster repeated searches
- **Export/Import**: Share knowledge bases

### Experimental Features

- **RAG Integration**: Retrieval-augmented generation
- **Semantic Clustering**: Auto-categorize documents
- **Entity Extraction**: Named entity recognition
- **Graph Relationships**: Knowledge graph construction

---

## 📚 References

### Technical Documentation

- [Technical Design v1.1](../../docs/technical-design-v1.1.md)
- [Email Connector Guide](../../docs/email-connector-guide.md)
- [API Reference](../../docs/api-reference.md)

### Research

- [Agent Interaction Pattern](../../docs/research/agent-interaction/)
- [Agent Society Architecture](../../docs/research/agent-society/)

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.1 | 2026-03-07 | Initial skill definition with core tools |
| v1.0 | 2026-02-15 | Project conception |

---

**Maintained by**: Integration Team  
**Contact**: Create an issue at GitHub repository  
**License**: MIT
