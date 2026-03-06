# Agent 经验总结

> 📝 各 Agent 在任务完成后的经验总结

**维护者**: 各 Agent  
**整理者**: PM Agent  

---

## 目录结构

```
experiences/
├── pm/          # PM Agent 的经验总结
├── data/        # Data Team 的经验总结
├── template/    # Template Team 的经验总结
├── test/        # Test Team 的经验总结
└── research/    # Research Agent 的经验总结
```

---

## 使用方式

### Agent 记录经验

每个 Agent 完成任务后，在各自目录下创建经验总结文件：

```
experiences/<agent>/<任务名>.md
```

### 经验总结格式

```markdown
# [任务名称] - 经验总结

**日期**: YYYY-MM-DD
**Agent**: [名称]
**任务**: [任务描述]

---

## 遇到的问题

### 问题1: [问题标题]

- **原因**: ...
- **解决**: ...
- **是否框架相关**: 是/否

---

## 有效做法

- 做法1: ...
- 做法2: ...

---

## 无效做法

- 做法1: ...
- **原因**: ...

---

## 改进建议

- **对框架的建议**: ...（会传递给 Research Agent）
- **对实践的建议**: ...
```

---

## 问题分类指南

### 框架相关问题

以下问题应该标记为"框架相关"，会传递给 Research Agent：

- Agent 交互模式问题
- 文档体系设计问题
- Context 管理问题
- Token-Based 管理问题
- 边界隔离机制问题
- 方法论层面问题

### 实践相关问题

以下问题标记为"实践相关"，由 PM Agent 处理：

- 具体技术实现问题
- 项目特定问题
- 工具使用问题
- 个人能力问题

---

## PM Agent 整理流程

1. 定期检查各 Agent 的经验文档
2. 提取框架相关问题 → `practice/issues/framework-related.md`
3. 提取实践相关问题 → `practice/issues/practice-related.md`
4. 向用户汇报重要问题

---

**维护者**: 各 Agent  
**整理者**: PM Agent  
**最后更新**: 2026-03-06
