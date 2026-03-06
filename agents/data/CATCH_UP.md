---
version: 2.0
last_update: 2026-03-06
agent: data
---

# Data Team - 启动文档

> 🔄 **启动时读取此文档** - 快速了解当前状态和工作

---

## Quick Status

**Last Updated**: 2026-03-06 02:15  
**Status**: 🟢 Ready to Merge  
**Current Task**: PR #19 已批准，需要 rebase 到最新 main  
**Progress**: 等待 rebase 后合并

---

## Who You Are

**Role**: Data System Developer  
**Team**: Data Team (`agents/data/`)  
**Expertise**: 元数据解析、数据验证、工具函数、算法实现

---

## Current Phase

**Phase**: Sprint 1 - PR Integration  
**Sprint Day**: 2/14

### Current Task
✅ PR #19 已通过审查，准备合并

**需要操作**: Rebase 到最新 main 分支

---

## Module Boundaries (当前实际结构)

### ✅ You Own
```
scripts/
├── types.py               # 类型定义
├── metadata_parser.py     # 元数据解析器
├── utils.py               # 工具函数 (在PR #19中)
└── tools/                 # 工具脚本
    ├── organize_notes.py
    ├── generate_index.py
    └── extract_keywords.py
```

**未来将扩展**（重构后）:
```
scripts/
├── core/
│   ├── types.py
│   ├── schema.py
│   └── validators.py
├── parsers/
│   ├── metadata_parser.py
│   ├── document_parser.py
│   └── yaml_parser.py
└── utils/
    ├── file_ops.py
    ├── data_ops.py
    └── text_ops.py
```

### ❌ You Do NOT Own (Template Team's Modules)
```
templates/                 # Template Team
scripts/
├── template_engine.py     # Template Team (未来)
├── config.py              # Template Team (未来)
└── tools/
    └── create_document.py # Template Team
```

---

## Active PRs & Issues

| Item | Status | Action Needed |
|------|--------|---------------|
| PR #19 | 🟢 待合并 | Rebase到最新main后可合并 |
| Issue #15 | ✅ 完成 | PR #19 已实现 |

---

## Next Actions

### 🟢 Immediate (现在)
1. **Rebase PR #19 到最新 main**
   ```bash
   # 在main仓库
   git checkout feature/b-utils-c
   git fetch origin
   git rebase origin/main
   git push -f origin feature/b-utils-c
   ```

2. **确认CI通过后通知PM**

### 🟡 After PR Merged
1. 开始工具脚本开发 (Issue待分配)
   - organize_notes.py
   - generate_index.py
   - extract_keywords.py

---

## Startup Checklist

- [ ] 读取 `agents/data/CATCH_UP.md` (本文件)
- [ ] 读取 `agent-status.md` 了解项目状态
- [ ] 切换到main仓库: `cd ../knowledge-assistant`
- [ ] 拉取最新代码: `git pull origin main`
- [ ] 检查分配的Issues

---

## Public APIs You Provide

```python
# 其他Agent可以导入使用
from scripts.types import DocumentMetadata, Document
from scripts.metadata_parser import MetadataParser
from scripts.utils import read_file, write_file, ensure_directory

# 使用示例
metadata = DocumentMetadata(title="Test", date="2026-03-06")
parser = MetadataParser()
meta, body = parser.parse(document_content)
```

---

## Status Update

**完成后更新** `agent-status.md`:
```markdown
### Data Team
| Field | Value |
|-------|-------|
| Status | 🟢 Ready to Merge |
| Current Task | PR #19 rebased, waiting for merge |
| Last Activity | YYYY-MM-DD HH:MM |
| Next Action | [下一步] |
```

---

## Quick Reference

- 项目状态: `agent-status.md`
- 核心指南: `agents/data/ESSENTIALS.md`
- 详细指南: `agents/data/guides/`
- PM文档: `agents/pm/AGENTS.md`

---

## Need Help?

1. 查看 `agents/data/ESSENTIALS.md` 详细说明
2. 在Issue中提问
3. 更新 `agent-status.md` 标记为 Blocked
4. 等待PM协助

---

**Remember**: 只修改 `scripts/types.py`, `scripts/metadata_parser.py`, `scripts/utils.py`, `scripts/tools/` 模块
