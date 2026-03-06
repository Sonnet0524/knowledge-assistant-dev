# Knowledge Assistant - Development Repository

> 本仓库包含 Knowledge Assistant 项目的开发过程资料，仅供开发团队内部使用。

## 🎯 仓库定位

- **类型**：Private（私有仓库）
- **目的**：团队协作和项目管理
- **受众**：开发团队（PM Agent、成员 Agents）

## 📦 仓库关系

```
knowledge-assistant-dev (Private)          knowledge-assistant (Public)
开发过程管理                                 输出交付品
         │                                           │
         └──────────── Git Push ──────────────────────┘
```

## 📚 内容导航

### Agent 配置
- **[OpenCode Agent使用指南](AGENTS_USAGE.md)** - ⭐ 如何启动和使用4个agent
- [PM Agent](agents/pm/AGENTS.md) - 项目管理智能体
- [成员 A Agent](agents/member-a/AGENTS.md) - 模板和配置模块开发
- [成员 B Agent](agents/member-b/AGENTS.md) - 元数据和工具模块开发
- [成员 Test Agent](agents/test/AGENTS.md) - 测试和质量保证

### 开发指南
- [工作流程](development-guide/workflow.md) - 整体开发流程
- [跨仓库工作流](development-guide/cross-repo-workflow.md) - ⭐ 双仓库协作
- [Git 工作流](development-guide/git-workflow.md) - ⭐ Git 规范
- [推送规则](development-guide/push-rules.md) - ⭐ 代码推送规范

### 项目管理
- [路线图](project-management/roadmap.md) - 项目总体规划
- [里程碑](project-management/milestones.md) - 里程碑计划
- [Issue 管理](project-management/issue-management.md) - Issue 流程

## 🚀 快速开始

### 1. 克隆仓库

```bash
# 克隆开发仓库
git clone https://github.com/Sonnet0524/knowledge-assistant-dev.git

# 克隆主仓库
git clone https://github.com/Sonnet0524/knowledge-assistant.git
```

### 2. 使用OpenCode启动Agent

本项目已配置OpenCode Agent系统，可以直接启动：

```bash
# 启动PM Agent（在dev仓库）
opencode --agent pm

# 启动Agent A/B/Test（在主仓库）
cd ../knowledge-assistant
opencode --agent member-a
opencode --agent member-b
opencode --agent test
```

详细使用说明请查看 [OpenCode Agent使用指南](AGENTS_USAGE.md)。

### 3. 阅读配置

每个 Agent 应该先阅读对应的 AGENTS.md 配置文件，了解自己的职责和规范。

### 4. 开始工作

按照 [工作流程](development-guide/workflow.md) 开始开发。

## 📋 开发流程概览

```
1. PM 创建 Issue（主仓库）
2. PM 分配 Issue 给 Agent
3. Agent 认领 Issue
4. Agent 开发（主仓库）
5. Agent 提交代码
6. PM Review
7. 合并到主分支
8. 发布
```

## 🔐 访问控制

- **主仓库**：Public，任何人可见
- **开发仓库**：Private，仅团队成员可见

## 📝 文档约定

- 所有文档使用 Markdown 格式
- 文档必须有版本号和更新日期
- 重要文档需要 Review

---

**版本**: v1.0  
**更新日期**: 2026-03-05  
**维护者**: PM Agent
