# 问题收集机制

> 📋 实践过程中问题和经验的收集与反馈机制

**维护者**: PM Agent  
**创建日期**: 2026-03-06

---

## 🎯 目的

将实践过程中发现的问题和积累的经验，系统化地反馈到框架研究中：

```
实践发现 → PM收集整理 → Research研究 → 框架改进
```

---

## 📁 目录结构

```
practice/issues/
├── README.md                # 本文件 - 机制说明
├── framework-related.md     # 框架相关问题（Research Agent 研究）
├── practice-related.md      # 实践层问题（PM Agent 处理）
└── resolved.md              # 已解决的问题记录
```

---

## 🔄 工作流程

### 1. Agent 发现问题

Agent 在工作过程中发现问题后：

1. 记录到 `practice/knowledge-base/experiences/<agent>/[任务名].md`
2. 标明是否为框架相关问题
3. 通知 PM Agent（通过状态更新）

### 2. PM Agent 收集整理

PM Agent 定期检查各 Agent 的经验文档，将问题分类：

- **框架相关** → 写入 `framework-related.md`
- **实践相关** → 写入 `practice-related.md`

### 3. Research Agent 研究

Research Agent 定期读取 `framework-related.md`，研究框架层面问题，产出改进文档。

---

## 📝 问题分类标准

### 框架相关问题

写入 `framework-related.md`，由 Research Agent 研究：

- Agent 交互模式问题
- 文档体系设计问题
- Context 管理问题
- Token-Based 管理问题
- 边界隔离机制问题
- 方法论层面问题

### 实践相关问题

写入 `practice-related.md`，由 PM Agent 处理：

- 具体技术实现问题
- 项目特定问题
- Agent 个人能力问题
- 工具使用问题

---

## 📋 相关文档

- [框架相关问题](framework-related.md)
- [实践相关问题](practice-related.md)
- [已解决问题](resolved.md)
- [Agent经验文档](../knowledge-base/experiences/)

---

**维护者**: PM Agent  
**最后更新**: 2026-03-06
