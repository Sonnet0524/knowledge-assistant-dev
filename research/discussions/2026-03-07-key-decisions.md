---
date: 2026-03-07
type: decision-record
subject: Agent Team Framework - 关键决策记录
participants: Human + Research Agent
---

# Agent Team Framework - 关键决策记录

## 📋 决策概述

**日期**: 2026-03-07  
**背景**: 基于理论vs实践对比分析，讨论7个关键议题  
**参与者**: Human + Research Agent  

---

## 🎯 决策记录

### 决策1：PM主动性边界

**讨论议题**：PM是否需要增加主动检查场景？

**Human决策**：
```
目前PM主动性受OpenCode限制，暂时不进行优化。

原因：
  - OpenCode架构限制
  - PM被动响应是架构约束，不是设计缺陷
  - 暂时接受当前模式

后续：
  - 等待OpenCode支持更好的机制
  - 或考虑其他架构方案
```

**Research Agent记录**：
- 状态：✅ 决策已确定
- 方案：保持PM被动响应模式
- 优先级：降为P2（长期优化）
- 备注：这是架构限制，不是紧急问题

---

### 决策2：Skills加载机制

**讨论议题**：Skills如何被Agent加载和使用？

**Human决策**：
```
目前Skills嵌入AGENTS.md是合理的，避免对skills的支持差异。

原因：
  - 避免依赖opencode的新功能
  - 嵌入方式简单可靠
  - 减少实施复杂度

方案：
  - Skills内容以适当方式嵌入AGENTS.md
  - 或在AGENTS.md中明确引用Skills文档路径
  - Agent按需读取Skills文档
```

**Research Agent记录**：
- 状态：✅ 决策已确定
- 方案：Skills嵌入/引用AGENTS.md
- 实施方式：
  ```markdown
  # 在AGENTS.md中引用Skills
  
  ## 相关Skills
  
  详见：
  - Git工作流：`framework/skills/workflow/git-workflow.md`
  - Review流程：`framework/skills/workflow/review-process.md`
  - 质量门控：`framework/skills/decision-support/quality-gate.md`
  
  Agent应按需读取这些Skills文档。
  ```
- 优先级：P0（Phase 1实施）

---

### 决策3：Agent间直接通信

**讨论议题**：如何实现Agent间通信？

**Human决策**：
```
目前Agent间通信受OpenCode限制。

实现方案：
  下达：由PM启动后台nohup进程（subagent）方式执行
  反馈：由文件记录

工作流程：
  1. PM Agent创建任务文件（如task-AI1.md）
  2. PM Agent启动后台进程（nohup opencode --agent ai &）
  3. AI Agent读取任务文件，执行任务
  4. AI Agent将结果写入文件（如result-AI1.md）
  5. PM Agent被动由Human唤醒
  6. PM Agent检查结果文件，更新状态
```

**Research Agent记录**：
- 状态：✅ 决策已确定
- 方案：后台进程 + 文件记录
- 实现细节：
  ```bash
  # PM启动AI Team（后台进程）
  nohup opencode --agent ai > logs/ai-team.log 2>&1 &
  
  # PM检查AI Team结果
  cat results/result-AI1.md
  ```
- 优势：
  - 突破OpenCode的Agent间通信限制
  - 支持并行执行多个Agent
  - 结果持久化，可追溯
- 劣势：
  - 需要Human唤醒PM检查结果
  - 文件管理需要规范
- 优先级：P1（可在Phase 2实施）
- 备注：这是一个创新的解决方案

---

### 决策4：记忆压缩机制

**讨论议题**：如何实现记忆压缩？

**Human决策**：
```
记忆压缩具体实现模式具有难度，如何压缩且保留关键信息。
这个列一个单独的课题，我们需要专门讨论。

研究需求：
  - 压缩算法设计
  - 关键信息保留策略
  - 压缩时机和触发条件
  - 压缩效果评估
```

**Research Agent记录**：
- 状态：⚠️ 需要专门研究
- 优先级：P1（短期研究课题）
- 下一步：
  - 创建专门的研究框架
  - 分析压缩需求和挑战
  - 设计压缩策略
- 备注：见 `research/proposals/memory-compression-research.md`（待创建）

---

### 决策5：元认知意识

**讨论议题**：如何实现元认知意识？

**Human决策**：
```
元认知怎么实现，还没进行设计。

状态：
  - 理论设计已有
  - 实现方案待设计
  - 需要进一步研究
```

**Research Agent记录**：
- 状态：⚠️ 待设计
- 优先级：P1（需要设计方案）
- 下一步：
  - 分析元认知意识的实现难点
  - 设计简化的实现方案
  - 与OpenClaw的实现对比
- 备注：暂不实施，先完成其他P0任务

---

### 决策6：Research Agent的职责

**Human强调**：
```
你是research，你不实现。

职责边界：
  ✅ 理论研究
  ✅ 框架设计
  ✅ 方案设计
  ✅ 问题分析
  
  ❌ 代码实现
  ❌ 配置修改
  ❌ 文档创建（实施层）
  ❌ 具体操作
```

**Research Agent确认**：
- 状态：✅ 已明确
- 我的职责：辅助研究、设计思路、理论支撑
- 我的边界：不参与实施、不写代码、不修改配置
- 我的产出：
  - 研究文档
  - 设计方案
  - 分析报告
  - 给PM的实施建议（不是直接实施）

---

## 📊 决策影响分析

### 对Phase 1的影响

#### 已确定可实施：
1. ✅ **Skills机制**：嵌入AGENTS.md方式
   - 修改FRAMEWORK_UPGRADE_REQUEST.md
   - 明确Skills引用方式

2. ✅ **AGENTS.md精简**：继续进行
   - 移除重复内容
   - 引用Skills文档

3. ✅ **memory-index.yaml**：创建索引文件
   - 定义记忆路径和优先级
   - 作为规划文档，暂不实现加载机制

#### 延后实施：
4. ⏸️ **PM主动性优化**：受架构限制，暂不优化

5. ⏸️ **记忆压缩机制**：需要专门研究

6. ⏸️ **元认知意识**：需要设计方案

---

### 对架构的影响

#### 当前架构（调整后）：
```
Agent Team Framework v1.1

┌──────────────────────────────────────┐
│  协作机制（已调整）                   │
├──────────────────────────────────────┤
│  PM Agent（被动响应）                │
│    ↓                                 │
│  Human（唤醒PM检查结果）             │
│    ↓                                 │
│  Team Agent（后台进程执行）          │
│    ↓                                 │
│  文件记录（结果持久化）              │
│    ↓                                 │
│  PM Agent（被Human唤醒后检查）       │
└──────────────────────────────────────┘

Skills机制：
  Skills → 引用 → AGENTS.md

记忆系统：
  四层记忆 + memory-index.yaml（规划）
```

---

## 📝 待办事项

### Research Agent待办

#### P0：立即完成
- [ ] 更新FRAMEWORK_UPGRADE_REQUEST.md
  - 修改Skills加载方式（嵌入/引用）
  - 调整实施步骤

- [ ] 创建Agent间通信方案文档
  - 后台进程启动方式
  - 文件记录规范
  - PM检查流程

#### P1：短期研究
- [ ] 创建记忆压缩研究框架
  - 分析压缩需求和挑战
  - 设计压缩策略
  - 评估压缩效果

- [ ] 元认知意识实现方案设计
  - 简化版方案
  - 实施路径
  - 验证方法

---

## 🎯 决策总结

### 已确定决策（5项）
1. ✅ PM主动性：保持被动，受架构限制
2. ✅ Skills机制：嵌入/引用AGENTS.md
3. ✅ Agent间通信：后台进程 + 文件记录
4. ⏸️ 记忆压缩：单独研究课题
5. ⏸️ 元认知意识：待设计

### Research Agent职责
- ✅ 明确：只研究、设计、分析，不实现

### 下一步重点
1. 更新PM的实施建议（Skills方式）
2. 准备记忆压缩研究框架
3. 设计元认知意识实现方案

---

**记录者**: Research Agent  
**记录时间**: 2026-03-07  
**状态**: 决策已记录，待执行待办事项
