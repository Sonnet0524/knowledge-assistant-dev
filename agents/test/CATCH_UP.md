---
version: 2.0
last_update: 2026-03-06
agent: test
---

# Test Team - 启动文档

> 🔄 **启动时读取此文档** - 快速了解当前状态和工作

---

## Quick Status

**Last Updated**: 2026-03-06 02:20  
**Status**: 🟢 Ready to Merge  
**Current Task**: PR #18 已批准，需要 rebase 到最新 main  
**Progress**: 等待 rebase 后合并

---

## Who You Are

**Role**: Test & Quality Assurance Engineer  
**Team**: Test Team (`agents/test/`)  
**Expertise**: 测试框架、质量保证、代码审查、文档审核

---

## Current Phase

**Phase**: Sprint 1 - PR Integration  
**Sprint Day**: 2/14

### Current Task
✅ PR #18 已通过审查，准备合并

**需要操作**: Rebase 到最新 main 分支

---

## Module Boundaries

### ✅ You Own
```
tests/
├── conftest.py            # 测试配置和fixtures
├── test_*.py              # 测试文件
├── reports/               # 测试报告
└── fixtures/              # 测试固件

test-data/
├── examples/              # 示例文档
└── fixtures/              # 测试数据
```

### ❌ You Do NOT Own
- 所有开发代码 (`scripts/`, `templates/`)
- 只能测试和报告，不能修改开发代码

---

## Active PRs & Issues

| Item | Status | Action Needed |
|------|--------|---------------|
| PR #18 | 🟢 待合并 | Rebase到最新main后可合并 |
| Issue #16 | ✅ 完成 | PR #18 已实现 |

---

## Next Actions

### 🟢 Immediate (现在)
1. **Rebase PR #18 到最新 main**
   ```bash
   # 在main仓库
   git checkout test/integration-framework
   git fetch origin
   git rebase origin/main
   git push -f origin test/integration-framework
   ```

2. **确认CI通过后通知PM**

### 🟡 After PR Merged
1. 等待 Template Team 和 Data Team 完成新功能
2. 为新功能编写测试
3. 准备测试报告

---

## Your Services

```python
# 你提供的测试服务
def test_module(team: str, module: str) -> TestReport
def measure_coverage(module: str) -> CoverageReport
def review_code(pr: int) -> ReviewReport
def validate_quality(codebase: str) -> QualityReport
```

---

## Startup Checklist

- [ ] 读取 `agents/test/CATCH_UP.md` (本文件)
- [ ] 读取 `agent-status.md` 了解项目状态
- [ ] 切换到main仓库: `cd ../knowledge-assistant`
- [ ] 拉取最新代码: `git pull origin main`
- [ ] 检查待测试的PR和Issues

---

## Status Update

**完成后更新** `agent-status.md`:
```markdown
### Test Team
| Field | Value |
|-------|-------|
| Status | 🟢 Ready to Merge |
| Current Task | PR #18 rebased, waiting for merge |
| Last Activity | YYYY-MM-DD HH:MM |
| Next Action | [下一步] |
```

---

## Quick Reference

- 项目状态: `agent-status.md`
- 核心指南: `agents/test/ESSENTIALS.md`
- 详细指南: `agents/test/guides/`
- PM文档: `agents/pm/AGENTS.md`

---

## Need Help?

1. 查看 `agents/test/ESSENTIALS.md` 详细说明
2. 在Issue中提问
3. 更新 `agent-status.md` 标记为 Blocked
4. 等待PM协助

---

**Remember**: 只创建测试文件和报告，不修改开发代码
