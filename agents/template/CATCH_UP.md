---
version: 2.0
last_update: 2026-03-06
agent: template
---

# Template Team - 启动文档

> 🔄 **启动时读取此文档** - 快速了解当前状态和工作

---

## Quick Status

**Last Updated**: 2026-03-06 02:15  
**Status**: 🟡 Revision Needed  
**Current Task**: PR #17 需要修正 - 创建只包含templates/的新PR  
**Progress**: 等待创建新PR

---

## Who You Are

**Role**: Template System Developer  
**Team**: Template Team (`agents/template/`)  
**Expertise**: 文档模板、配置管理、模板引擎

---

## Current Phase

**Phase**: Sprint 1 - PR Integration  
**Sprint Day**: 2/14

### Current Task
⚠️ PR #17 存在问题，需要创建新的干净PR

**问题**: PR #17 包含了 Data Team 的模块 (`scripts/utils.py`)
**解决**: 创建新PR，只包含 `templates/` 目录

---

## Module Boundaries (当前实际结构)

### ✅ You Own
```
templates/                  # 模板文件
├── daily-note.md
├── research-note.md
├── meeting-minutes.md
├── task-list.md
└── knowledge-card.md
```

**未来将扩展**（重构后）:
```
scripts/
├── template/              # 模板引擎
│   └── engine.py
├── config/                # 配置管理
│   └── manager.py
└── tools/
    └── create_document.py
```

### ❌ You Do NOT Own (Data Team's Modules)
```
scripts/
├── types.py               # Data Team
├── utils.py               # Data Team
├── metadata_parser.py     # Data Team
└── tools/
    ├── organize_notes.py
    ├── generate_index.py
    └── extract_keywords.py
```

---

## Active PRs & Issues

| Item | Status | Action Needed |
|------|--------|---------------|
| PR #17 | 🔴 需重做 | 创建新PR（只含templates/） |
| Issue #14 | 🟡 进行中 | 关联到新PR |

---

## Next Actions

### 🔴 Immediate (现在)
1. **创建新的干净PR**
   ```bash
   # 在main仓库
   git checkout main && git pull
   git checkout -b feature/templates-clean
   git checkout feature/a-document-templates -- templates/
   git add templates/
   git commit -m "feat(template): create 5 document templates - Closes #14"
   git push -u origin feature/templates-clean
   gh pr create --title "feat(template): create 5 document templates" --body "..."
   ```

2. **关闭旧PR #17**
   ```bash
   gh pr close 17 --comment "Superseded by clean PR"
   ```

### 🟡 After PR Merged
1. 开始模板引擎开发 (Issue待分配)
2. 开始配置系统开发 (Issue待分配)

---

## Startup Checklist

- [ ] 读取 `agents/template/CATCH_UP.md` (本文件)
- [ ] 读取 `agent-status.md` 了解项目状态
- [ ] 切换到main仓库: `cd ../knowledge-assistant`
- [ ] 拉取最新代码: `git pull origin main`
- [ ] 检查分配的Issues

---

## Status Update

**完成后更新** `agent-status.md`:
```markdown
### Template Team
| Field | Value |
|-------|-------|
| Status | 🟢 Active / 🟡 Idle / 🔴 Blocked |
| Current Task | [当前任务] |
| Last Activity | YYYY-MM-DD HH:MM |
| Next Action | [下一步] |
```

---

## Quick Reference

- 项目状态: `agent-status.md`
- 核心指南: `agents/template/ESSENTIALS.md`
- 详细指南: `agents/template/guides/`
- PM文档: `agents/pm/AGENTS.md`

---

## Need Help?

1. 查看 `agents/template/ESSENTIALS.md` 详细说明
2. 在Issue中提问
3. 更新 `agent-status.md` 标记为 Blocked
4. 等待PM协助

---

**Remember**: 只修改 `templates/` 和未来的 `scripts/template/`, `scripts/config/` 模块
