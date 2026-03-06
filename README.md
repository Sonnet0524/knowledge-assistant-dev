# Knowledge Assistant - Agent Team Development Repository

> AI Agent协作开发的项目管理仓库

**版本**: v3.0  
**更新日期**: 2026-03-06  
**状态**: Active

---

## 📖 目录

- [项目概况](#项目概况)
- [Agent Team概念](#agent-team概念)
- [设计思路](#设计思路)
- [当前实践](#当前实践)
- [快速开始](#快速开始)
- [文档导航](#文档导航)

---

## 项目概况

### 仓库定位

- **类型**：Private（私有仓库）
- **目的**：AI Agent团队的协作和项目管理
- **受众**：AI Agent团队（PM、Data、Template、Test Agent）

### 双仓库架构

```
┌──────────────────────────────┐
│  knowledge-assistant-dev     │
│  (Private - 开发过程管理)     │
│                              │
│  - Agent配置                 │
│  - 项目规划                  │
│  - 知识库                    │
│  - 状态跟踪                  │
└──────────────────────────────┘
            │
            │ 协调、指导
            ↓
┌──────────────────────────────┐
│  knowledge-assistant         │
│  (Public - 输出交付品)        │
│                              │
│  - 项目代码                  │
│  - 用户文档                  │
│  - 测试代码                  │
└──────────────────────────────┘
```

---

## Agent Team概念

### 什么是Agent Team？

**Agent Team**是由多个专用AI Agent组成的协作开发团队。每个Agent有明确的职责、独立的模块边界、专业的能力，通过规范的协作流程共同完成项目开发。

### 团队成员

| Agent | 角色 | 职责 | 模块 |
|-------|------|------|------|
| **PM** | 项目经理 | 规划、协调、Review、用户交互 | 项目管理 |
| **Data** | 数据专家 | 类型定义、解析器、工具函数 | 数据层 |
| **Template** | 模板专家 | 模板引擎、配置系统 | 应用层 |
| **Test** | 质量专家 | 测试框架、质量保证 | 质量层 |

### 核心特性

1. **专业化**：每个Agent专注特定领域
2. **独立性**：模块边界清晰，零交叉
3. **协作性**：通过规范接口协作
4. **可控性**：PM统一协调管理

---

## 设计思路

### 核心原则

#### 1. Agent First vs Human First

**Agent First**（Agent间通信）：
- 格式：结构化、简洁、机器可读
- 示例：CATCH_UP.md, ESSENTIALS.md
- 目的：高效、精准

**Human First**（用户交互）：
- 格式：人性化、易读、有温度
- 示例：HUMAN_ADMIN.md, 用户报告
- 目的：易懂、友好

**设计决策**：
```
Agent间通信 → Agent First (简洁高效)
PM→用户    → PM转化为Human First (易懂友好)
```

#### 2. Context窗口最小化

**问题**：AI Agent启动时context有限，需要最小化必需加载的信息

**策略**：
- **分层文档**：必需(<50行) → 按需(<100行) → 可选
- **按需披露**：只读必需信息，详细指南按需加载
- **索引机制**：知识库通过索引检索，不预加载

**效果**：
- Context使用：从~600行降至~40行
- **节省：93%** ✅

#### 3. 上下文边界隔离

**定义**：每个Agent的模块完全不重叠，零交叉修改

**目的**：
- 避免冲突
- 清晰职责
- 独立开发
- 单向依赖

**实现**：
- Data Agent: 数据层（无外部依赖）
- Template Agent: 应用层（依赖Data）
- Test Agent: 质量层（测试所有）
- PM Agent: 管理层（协调所有）

#### 4. Token-Based进度管理

**问题**：自然日/周不适合Agent工作模式

**解决方案**：基于Token消耗的时间单位

| 单位 | 定义 | 示例 |
|------|------|------|
| **Task** | 单个Issue | 实现YAML解析器 (1,200 tokens) |
| **Checkpoint** | 相关Tasks集合 | 元数据解析器 (5,000 tokens) |
| **Phase** | 功能模块 | 核心数据系统 (15,000 tokens) |

**优势**：
- 精确预估工作量
- 实时进度跟踪
- 准确ETC预测
- 不依赖自然时间

---

## 当前实践

### 已实现的成果

#### ✅ 文档体系

**分层文档结构**：
```
agents/
├── data/
│   ├── CATCH_UP.md      # Level 0 - 必需 (<50行)
│   ├── ESSENTIALS.md     # Level 1 - 按需 (<100行)
│   └── guides/           # Level 2 - 可选
├── template/
│   ├── CATCH_UP.md
│   ├── ESSENTIALS.md
│   └── guides/
├── test/
│   ├── CATCH_UP.md
│   ├── ESSENTIALS.md
│   └── guides/
└── pm/
    ├── CATCH_UP.md
    ├── ESSENTIALS.md
    └── guides/
```

#### ✅ 项目管理

**Token-Based规划**：
- `project-management/phases.md` - Phase规划
- `agent-status.md` - 实时状态跟踪
- Token消耗统计和velocity分析

#### ✅ 知识管理

**按需检索的知识库**：
```
knowledge-base/
├── INDEX.md              # 知识索引
├── experiences/          # 经验库
├── decisions/            # 决策库
└── patterns/             # 模式库
```

#### ✅ 工具配置

**OpenCode集成**：
- `opencode.json` - Agent配置
- 自动读取CATCH_UP.md
- 权限精细控制

### 项目进展

**当前进度**：Token: 24,500 / 55,000 (45%)

| Phase | Owner | Progress | Status |
|-------|-------|----------|--------|
| Phase 1: 核心数据系统 | Data | 73% | Active |
| Phase 2: 文档模板系统 | Template | 18% | Active |
| Phase 3: 质量保证体系 | Test | 25% | Active |
| Phase 4: 集成与优化 | PM | 0% | Planned |

**已完成的Checkpoints**：
- ✅ 类型系统（Data Agent）
- ✅ 元数据解析器（Data Agent）
- ✅ 测试框架（Test Agent）
- ✅ 集成测试框架（Test Agent）

**正在进行**：
- ⏳ 工具函数（Data Agent）
- ⏳ 模板引擎核心（Template Agent）

### 改进效果

| 指标 | 之前 | 现在 | 改进 |
|------|------|------|------|
| **Context使用** | ~600行 | ~40行 | ↓ 93% |
| **模块边界** | 有交叉 | 100%隔离 | ✓ |
| **时间管理** | 自然日/周 | Token-based | ✓ |
| **知识检索** | 全量加载 | 按需检索 | ↓ 80% |

---

## 快速开始

### 1. 环境准备

```bash
# 克隆开发仓库
git clone https://github.com/Sonnet0524/knowledge-assistant-dev.git

# 克隆主仓库
git clone https://github.com/Sonnet0524/knowledge-assistant.git

# 安装OpenCode (如果还没有)
# 参考: https://opencode.ai
```

### 2. 启动Agent

```bash
# 进入开发仓库
cd knowledge-assistant-dev

# 启动PM Agent（项目管理）
opencode --agent pm

# 启动Data Agent（数据开发）
# 先切换到主仓库
cd ../knowledge-assistant
opencode --agent data

# 启动Template Agent（模板开发）
opencode --agent template

# 启动Test Agent（测试）
opencode --agent test
```

### 3. Agent会自动执行

1. 读取CATCH_UP.md（<50行，必需）
2. 了解当前状态和任务
3. 切换到工作仓库
4. 拉取最新代码
5. 查看分配的Issues
6. 开始工作

### 4. 按需加载详细信息

```bash
# 如需核心职责
cat agents/data/ESSENTIALS.md

# 如需详细指南
ls agents/data/guides/

# 如需经验参考
cat knowledge-base/INDEX.md
```

---

## 文档导航

### 📚 核心文档

**设计文档**：
- **[AGENT_TEAM_DESIGN.md](AGENT_TEAM_DESIGN.md)** - ⭐ Agent Team全面设计文档
- **[REFACTOR_REPORT.md](REFACTOR_REPORT.md)** - 重构完成报告
- **[AGENTS_USAGE.md](AGENTS_USAGE.md)** - OpenCode Agent使用指南

**项目规划**：
- **[project-management/phases.md](project-management/phases.md)** - ⭐ Token-based项目规划
- [project-management/roadmap.md](project-management/roadmap.md) - 总体路线图
- [project-management/milestones.md](project-management/milestones.md) - 里程碑计划

**状态跟踪**：
- **[agent-status.md](agent-status.md)** - ⭐ Agent实时状态
- [HUMAN_ADMIN.md](HUMAN_ADMIN.md) - 用户项目总览

**知识库**：
- **[knowledge-base/INDEX.md](knowledge-base/INDEX.md)** - ⭐ 知识库索引

### 📂 Agent配置

**快速启动文档**（必需读取）：
- [PM Agent - CATCH_UP.md](agents/pm/CATCH_UP.md)
- [Data Agent - CATCH_UP.md](agents/data/CATCH_UP.md)
- [Template Agent - CATCH_UP.md](agents/template/CATCH_UP.md)
- [Test Agent - CATCH_UP.md](agents/test/CATCH_UP.md)

**核心职责**（按需读取）：
- [PM Agent - ESSENTIALS.md](agents/pm/ESSENTIALS.md)
- [Data Agent - ESSENTIALS.md](agents/data/ESSENTIALS.md)
- [Template Agent - ESSENTIALS.md](agents/template/ESSENTIALS.md)
- [Test Agent - ESSENTIALS.md](agents/test/ESSENTIALS.md)

### 🛠️ 开发指南

- [development-guide/workflow.md](development-guide/workflow.md) - 工作流程
- [development-guide/cross-repo-workflow.md](development-guide/cross-repo-workflow.md) - 跨仓库协作
- [development-guide/git-workflow.md](development-guide/git-workflow.md) - Git规范
- [development-guide/push-rules.md](development-guide/push-rules.md) - 代码推送规范

---

## 开发流程

```
1. PM 创建 Issue（主仓库，基于Phase规划）
   ↓
2. PM 分配 Issue 给对应 Agent
   ↓
3. Agent 认领 Issue，更新状态
   ↓
4. Agent 开发（主仓库，TDD）
   ↓
5. Agent 提交 PR，更新状态
   ↓
6. PM Review，提供反馈
   ↓
7. Agent 修改直至通过
   ↓
8. PM 合并到主分支
   ↓
9. Agent 总结经验到知识库
   ↓
10. PM 更新进度，生成报告
```

---

## 关键特性

### ✅ Context最小化
- 启动时只读<50行必需信息
- 节省93% context窗口

### ✅ 模块边界隔离
- 100%模块不重叠
- 零冲突可能

### ✅ Token-Based管理
- 精确预估工作量
- 实时进度跟踪
- 不依赖自然时间

### ✅ 按需知识检索
- 索引快速定位
- 不预加载知识库
- 节省80%检索时间

### ✅ 双原则设计
- Agent First: Agent间通信高效
- Human First: 用户体验友好

---

## 适用场景

本Agent Team设计适用于：

- ✅ AI Agent协作开发项目
- ✅ 多模块并行开发
- ✅ 需要精确进度跟踪
- ✅ 知识密集型项目
- ✅ 长期维护的项目

---

## 技术栈

- **AI平台**: OpenCode
- **项目管理**: Token-based tracking
- **知识管理**: Markdown + Git
- **协作工具**: GitHub Issues & PRs
- **版本控制**: Git

---

## 访问控制

- **开发仓库**（本仓库）：Private，仅Agent团队可见
- **主仓库**：Public，用户可见最终交付品

---

## 维护说明

**文档维护**：
- PM Agent负责整体维护
- 各Agent维护自己的CATCH_UP.md
- 知识库由贡献者维护，PM审核

**更新频率**：
- agent-status.md: 实时
- CATCH_UP.md: 任务变化时
- phases.md: Checkpoint完成时
- 本README: 有重大变更时

---

## 相关链接

- [OpenCode官方文档](https://opencode.ai)
- [主仓库: knowledge-assistant](https://github.com/Sonnet0524/knowledge-assistant)
- [问题反馈](https://github.com/Sonnet0524/knowledge-assistant-dev/issues)

---

**维护者**: PM Agent  
**创建时间**: 2026-03-05  
**最后更新**: 2026-03-06
