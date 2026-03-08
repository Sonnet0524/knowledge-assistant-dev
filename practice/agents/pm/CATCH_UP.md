# PM Team - 启动文档

> 🔄 **启动时读取此文档** - 快速了解当前状态和工作

---

## Quick Status

**Last Updated**: 2026-03-08 (v1.1 Released 🎉)  
**Current Phase**: v1.1 Released ✅  
**Status**: 🟢 Complete - v1.1.0 已发布  
**Version**: v1.1.0

---

## Current Focus

**Primary Task**: v1.1 发布完成 ✅

**Completed Actions**:
1. ✅ Sprint 1完成（AI Team + Test Team）
2. ✅ Sprint 2完成（Core Team + Integration Team）
3. ✅ Sprint 3完成（Integration Team + Test Team）
4. ✅ Test Team集成测试通过 (91.7%)
5. ✅ **v1.1.0 发布完成**
   - RELEASE_NOTES.md 已更新
   - README.md 已更新
   - GitHub Release 已创建
   - Tag v1.1.0 已推送

**Release URL**: https://github.com/Sonnet0524/knowledge-assistant/releases/tag/v1.1.0

---

## 今日工作总结 (2026-03-08)

### 主要成果 - v1.1.0 发布 ✅

#### 1. 发布准备完成 ✅
- 更新 RELEASE_NOTES.md
- 更新 README.md
- 合并 PR #36 (extraction tools)
- 创建并推送 v1.1.0 tag
- 创建 GitHub Release

#### 2. v1.1 功能清单 ✅
| 功能 | Team | 状态 |
|------|------|------|
| 语义索引构建 | AI Team | ✅ |
| 语义搜索 | AI Team | ✅ |
| 关键词提取 | Core Team | ✅ |
| 摘要生成 | Core Team | ✅ |
| 邮件连接器 | Integration Team | ✅ |
| opencode集成 | Integration Team | ✅ |

---

## 历史工作总结 (2026-03-07)
- 执行时间: 8.88s

**Sprint 2验证**:
- ✅ Issue #8: extract_keywords() 已实现并通过测试
- ✅ Issue #9: generate_summary() 已实现并通过测试
- ✅ PR #17: 已合并到 main 分支
- ✅ 所有性能指标达标

**发布建议**: ✅ **建议发布 v1.1**

**报告位置**: `reports/test-report.md`

---

## Team Status

| Team | Status | Location | Current Task |
|------|--------|----------|--------------|
| PM Team | 🟢 Active | agents/pm/ | 准备v1.1发布 |
| Core Team | ✅ Complete | agents/core/ | Sprint 2完成 |
| AI Team | ✅ Complete | agents/ai/ | Sprint 1完成 |
| Integration Team | ✅ Complete | agents/integration/ | Sprint 2-3完成 |
| Test Team | ✅ Complete | agents/test/ | 集成测试完成 |
| Research | 🔒 External | agents/research/ | 外部Agent，不受管控 |

---

## Project Context

### Repositories
- **Dev Repo**: `D:\opencode\knowledge-assistant-dev` (当前工作目录)
- **Main Repo**: `../knowledge-assistant` (代码仓库)

### v1.1 Architecture
```
opencode (Master Agent)
  ├── 文件操作 (own capability)
  ├── NLU & 理解 (own capability)
  └── 调用 knowledge-assistant tools
      ↓
knowledge-assistant (Tool Library)
  ├── AI Team: 语义索引+搜索
  ├── Core Team: 知识提取
  └── Integration Team: 连接器+集成
```

### v1.1 Sprint Plan
- **Sprint 1** (Week 1-2): AI Team - 索引+搜索 ✅ 完成
- **Sprint 2** (Week 3-4): Core Team + Integration Team - 提取+连接器 ✅ 完成
- **Sprint 3** (Week 5-6): Integration Team - 集成+发布 ✅ 开发完成，测试中

---

## 🚀 启动流程

**在dev仓库启动，操作main仓库时使用路径**

### 1. 读取状态文档
```bash
# 已在dev仓库，直接读取
practice/agents/pm/CATCH_UP.md    # 本文件
practice/status/agent-status.md   # 团队状态
practice/status/human-admin.md    # 用户总览
```

### 2. 同步代码仓库
```bash
# 同步dev仓库
git pull origin main

# 同步main仓库（使用相对路径）
cd ../knowledge-assistant
git pull origin main
cd ../knowledge-assistant-dev
```

### 3. 确认当前任务
- 检查本文件中的"Current Focus"
- 检查 `agent-status.md` 中各Team状态
- 检查 `status/task-assignments/v1.1-task-assignments.md`

---

## Working Directory

**启动位置**: `D:\opencode\knowledge-assistant-dev` (dev仓库)

**操作main仓库时**:
- 相对路径: `../knowledge-assistant`
- 或使用工具的 `workdir` 参数

---

## Key Files to Reference

### Planning Documents
- `status/task-assignments/v1.1-task-assignments.md` - v1.1任务分配
- `../knowledge-assistant/docs/PRD.md` - 产品需求文档

### Team Status
- `status/agent-status.md` - All teams status tracking

### Team Configs
- `agents/pm/AGENTS.md` - PM Team config
- `agents/core/AGENTS.md` - Core Team config
- `agents/ai/AGENTS.md` - AI Team config
- `agents/integration/AGENTS.md` - Integration Team config
- `agents/test/AGENTS.md` - Test Team config

### Startup Scripts
- `start-pm.bat/sh` - PM Team启动
- `start-core.bat/sh` - Core Team启动
- `start-ai.bat/sh` - AI Team启动
- `start-integration.bat/sh` - Integration Team启动
- `start-test.bat/sh` - Test Team启动

---

## Pending Tasks

### High Priority
- [x] 读取Test Team报告 ✅
  - reports/test-report.md - 已读取
  - 测试通过率: 91.7%
  - 发布建议: ✅ 建议发布 v1.1

- [ ] 完成v1.1发布准备（Issue #15）
  - 准备Release Notes
  - 更新版本号
  - 创建发布文档

### Medium Priority
- [ ] 总结v1.1开发经验
- [ ] 更新项目文档

---

## Status Update

**更新 `agent-status.md`**:
- 用户询问后更新
- Agent报告问题后记录
- 任务分配后跟踪
- Review完成后记录

**工作模式**:
- ✅ **主动启动Agent** - 分配任务后立即启动
- ❌ **不轮询状态** - 不主动检查Agent进度
- ✅ **被动接收报告** - 等待Agent报告

**Agent启动方法**:
详见 `practice/agents/pm/WORKFLOW.md`

```bash
opencode run --agent <name> "message" > logs/<team>.log 2>&1 &
```

---

## Quick Reference

| 文档 | 路径 |
|------|------|
| 启动文档 | `practice/agents/pm/CATCH_UP.md` |
| 核心指南 | `practice/agents/pm/ESSENTIALS.md` |
| **工作流程** | `practice/agents/pm/WORKFLOW.md` ⭐ |
| 团队状态 | `practice/status/agent-status.md` |
| 用户总览 | `practice/status/human-admin.md` |

---

## Important Notes

### Research Agent
- **状态**: 外部Agent，不受PM Team管控
- **权限**: PM Team不能修改Research Agent的任何内容
- **协作**: 向Research Team分享知识和经验

### Team结构变更流程
当Team结构变化时，必须同步更新：
1. opencode.json
2. practice/agents/{team}/AGENTS.md
3. practice/agents/{team}/CATCH_UP.md
4. start-{team}.bat 和 start-{team}.sh
5. agent-status.md 和 human-admin.md

---

**Remember**: 
- ✅ **主动启动Agent** - 分配任务后立即启动（opencode run）
- ❌ **不轮询状态** - 不主动检查Agent进度
- ✅ **被动接收报告** - Agent完成后读取报告
- ❌ **禁止使用task工具启动Team Agent** - task只能启动general/explore
- 在dev仓库启动和工作
- 操作main仓库时使用 `../knowledge-assistant` 或 `workdir` 参数
- 你是协调者，保持所有人同步
- v1.1核心：opencode集成，不重复opencode能力
- Research Agent是外部Agent，保持知识分享

---

**Last Updated**: 2026-03-07 21:00  
**Next Work**: 准备v1.1发布（Issue #15）
