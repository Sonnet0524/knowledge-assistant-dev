# 复刻实践指南

> 📖 如何在自己的项目中复刻 Agent Team 协作模式

**适用对象**: 想要使用Agent Team模式进行项目开发的实践者

---

## 📋 前置条件

### 1. 安装 OpenCode CLI

本项目使用 [OpenCode](https://opencode.ai) 作为Agent运行环境。

```bash
# 安装 OpenCode (请参考官方文档)
# https://opencode.ai/docs/installation
```

### 2. 克隆本仓库

```bash
git clone https://github.com/Sonnet0524/SG-AgentTeam.git
cd SG-AgentTeam
```

---

## 🚀 启动 Agent

### 方式一：使用启动脚本

```bash
# Linux/Mac
./start-pm.sh        # 启动 PM Agent
./start-data.sh      # 启动 Data Agent
./start-template.sh  # 启动 Template Agent
./start-test.sh      # 启动 Test Agent
./start-research.sh  # 启动 Research Agent

# Windows
start-pm.bat
start-data.bat
start-template.bat
start-test.bat
start-research.bat
```

### 方式二：使用 OpenCode 命令

```bash
opencode --agent pm        # 启动 PM Agent
opencode --agent data      # 启动 Data Agent
opencode --agent template  # 启动 Template Agent
opencode --agent test      # 启动 Test Agent
opencode --agent research  # 启动 Research Agent
```

### 启动后发生了什么？

每个Agent启动时会：
1. 读取 `CATCH_UP.md`（<50行，快速恢复上下文）
2. 了解当前状态和任务
3. 准备好接收指令

---

## 👥 Agent 角色说明

| Agent | 角色 | 启动命令 | 交互方式 |
|-------|------|---------|---------|
| **PM** | 项目管理者 | `./start-pm.sh` | 直接对话，分配任务、查看进度 |
| **Data** | 数据开发者 | `./start-data.sh` | 接收PM分配的任务，开发数据模块 |
| **Template** | 模板开发者 | `./start-template.sh` | 接收PM分配的任务，开发模板模块 |
| **Test** | 测试工程师 | `./start-test.sh` | 编写测试，保证质量 |
| **Research** | 框架研究者 | `./start-research.sh` | 研究框架设计，与用户讨论方法论 |

### 框架层 vs 实践层

```
框架层（通用）
├── Research Agent    → 研究Agent协作理论
└── docs/             → 框架文档

实践层（本项目）
├── PM Agent          → 管理本项目
├── Data Agent        → 开发本项目数据模块
├── Template Agent    → 开发本项目模板模块
└── Test Agent        → 测试本项目
```

---

## 🔄 典型工作流程

### 流程1: 开发新功能

```
┌─────────────────────────────────────────────────────────┐
│  User                                                   │
│   ↓ "我需要添加一个YAML解析功能"                          │
├─────────────────────────────────────────────────────────┤
│  PM Agent                                               │
│   ↓ 分析需求，创建任务，分配给 Data Agent                  │
│   ↓ 更新 agent-status.md                                │
├─────────────────────────────────────────────────────────┤
│  Data Agent                                             │
│   ↓ 接收任务，开发代码                                    │
│   ↓ 完成后提交 PR                                        │
├─────────────────────────────────────────────────────────┤
│  PM Agent                                               │
│   ↓ Review PR，合并代码                                  │
│   ↓ 更新状态                                             │
└─────────────────────────────────────────────────────────┘
```

**操作示例**:

```
# 1. 启动 PM Agent
./start-pm.sh

# 2. 告诉PM你的需求
User: "我需要添加一个YAML解析功能，解析文档的frontmatter元数据"

# 3. PM会自动：
#    - 分析需求
#    - 创建任务
#    - 分配给合适的Agent
#    - 跟踪进度

# 4. PM可能会问一些澄清问题，回答即可

# 5. 完成后，PM会汇报结果
```

### 流程2: 查看项目状态

```
# 启动 PM Agent
./start-pm.sh

# 询问状态
User: "项目现在进度如何？"

# PM会读取状态文档并汇报
```

### 流程3: 讨论框架设计

```
# 启动 Research Agent
./start-research.sh

# 讨论框架问题
User: "Agent之间的文档交互应该遵循什么原则？"

# Research Agent 会：
#    - 分析问题
#    - 提供设计思路
#    - 与你讨论
#    - 产出框架文档
```

---

## 💬 与 Agent 交互

### 与 PM Agent 交互

```
# 分配任务
"请实现XXX功能"

# 查看进度
"当前进度如何？"

# 解决问题
"Data Agent遇到了阻塞，请帮忙协调"

# 查看团队状态
"各Agent现在在做什么？"
```

### 与开发Agent交互（Data/Template）

```
# 通常不直接交互，通过PM分配任务
# 如果需要直接交互：

# 查看当前任务
"你现在在做什么？"

# 技术讨论
"这个模块的设计思路是什么？"
```

### 与 Test Agent 交互

```
# 运行测试
"请运行所有测试"

# 查看覆盖率
"当前测试覆盖率是多少？"

# 添加测试
"请为XXX功能添加测试"
```

### 与 Research Agent 交互

```
# 讨论框架设计
"Agent协作的最佳实践是什么？"

# 请求方法论指导
"如何设计文档分层体系？"

# 产出研究文档
"请输出关于XXX的研究报告"
```

---

## 📁 关键文件说明

### Agent状态文件

| 文件 | 作用 | 更新者 |
|------|------|--------|
| `practice/status/agent-status.md` | 各Agent当前状态 | PM Agent |
| `practice/status/human-admin.md` | 给用户的状态总览 | PM Agent |

### Agent配置文件

| 文件 | 作用 |
|------|------|
| `agents/research/CATCH_UP.md` | Research Agent启动入口 |
| `practice/agents/pm/CATCH_UP.md` | PM Agent启动入口 |
| `practice/agents/data/CATCH_UP.md` | Data Agent启动入口 |
| `practice/agents/template/CATCH_UP.md` | Template Agent启动入口 |
| `practice/agents/test/CATCH_UP.md` | Test Agent启动入口 |

### 项目管理文件

| 文件 | 作用 |
|------|------|
| `practice/management/roadmap.md` | 项目路线图 |
| `practice/management/milestones.md` | 里程碑定义 |
| `practice/management/sprint-*.md` | Sprint计划 |

---

## 🛠️ 自定义你的Agent Team

如果你想在自己的项目中使用这个模式：

### 1. 复制框架结构

```bash
# 保留框架层
docs/           # 框架文档
agents/research/ # Research Agent

# 创建你自己的实践层
practice/
├── agents/     # 你的Agent配置
├── management/ # 你的项目管理
└── ...
```

### 2. 修改Agent配置

编辑 `opencode.json`，调整Agent的：
- 职责描述
- 权限设置
- 启动文件路径

### 3. 编写Agent的CATCH_UP.md

每个Agent需要一个简洁的启动文件：

```markdown
---
agent: your-agent-name
status: Idle
last_update: YYYY-MM-DD
---

# Current Status

**Role**: 这个Agent的角色
**Responsibilities**: 负责什么

# Module Boundary

- 负责: xxx
- 不负责: xxx

# Quick Reference

- 相关文件: xxx
```

---

## ⚠️ 注意事项

### 1. 一个时间只启动一个Agent

```
✅ 正确: 启动PM → 完成任务 → 关闭 → 启动Data
❌ 错误: 同时启动多个Agent（可能造成状态混乱）
```

### 2. 任务完成后更新状态

```
PM Agent 负责更新:
- agent-status.md
- human-admin.md
- 任务分配文档
```

### 3. 遵守模块边界

```
每个Agent只修改自己负责的文件
跨模块修改需要通过PM协调
```

---

## 📚 延伸阅读

- [框架文档](../docs/) - Agent Team Framework 理论
- [Agent Team设计方法论](../docs/methodology/agent-team-design.md)
- [文档分层体系](../docs/methodology/document-hierarchy.md)

---

**维护者**: Research Agent  
**更新时间**: 2026-03-06
