# 实践信息反馈机制设计

> 📋 本文档说明如何将实践层的问题和经验反馈到框架研究中

**设计者**: Research Agent  
**执行者**: PM Agent  
**日期**: 2026-03-06

---

## 🎯 设计目标

让实践过程中发现的问题和积累的经验，能够**系统化地**反馈到框架研究中，形成：

```
实践发现 → PM收集整理 → Research研究 → 框架改进
```

---

## 📊 信息流设计

```
┌─────────────────────────────────────────────────────────┐
│                    实践层 Agent                          │
│            (PM/Data/Template/Test)                      │
│                                                         │
│  工作中发现问题 → 记录到个人经验文档                        │
│  完成任务后 → 总结经验到 knowledge-base/                  │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────────┐
│                    PM Agent                              │
│                                                         │
│  1. 收集各Agent的问题报告                                 │
│  2. 整理到 practice/issues/ 目录                         │
│  3. 维护 practice/issues/framework-related.md           │
│  4. 定期汇报给用户                                        │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────────┐
│                  Research Agent                          │
│                                                         │
│  1. 读取 practice/issues/framework-related.md           │
│  2. 提取框架层面问题                                      │
│  3. 研究并更新框架文档                                    │
│  4. 反馈研究结果                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 文档结构设计

### 新增目录

```
practice/
├── issues/                      # 🆕 问题收集目录
│   ├── README.md                # 问题收集说明
│   ├── framework-related.md     # 框架相关问题（给Research）
│   ├── practice-related.md      # 实践层问题（PM自己处理）
│   └── resolved.md              # 已解决的问题
│
├── knowledge-base/
│   └── experiences/             # 各Agent的经验总结
│       ├── pm/
│       ├── data/
│       ├── template/
│       └── test/
```

### 关键文件说明

| 文件 | 维护者 | 内容 | 读者 |
|------|--------|------|------|
| `issues/framework-related.md` | PM | 框架层面的问题 | Research Agent |
| `issues/practice-related.md` | PM | 实践层问题 | PM自己处理 |
| `issues/resolved.md` | PM | 已解决问题的记录 | 所有人 |
| `knowledge-base/experiences/*/` | 各Agent | 任务完成后的经验总结 | PM整理, Research参考 |

---

## 📝 文档格式设计

### 1. issues/framework-related.md 格式

```markdown
# 框架相关问题

> 📋 实践中发现的框架层面问题，供Research Agent研究

**维护者**: PM Agent  
**最后更新**: YYYY-MM-DD

---

## 待研究问题

### 问题-001: [问题标题]

- **发现时间**: YYYY-MM-DD
- **发现者**: [Agent名称]
- **问题描述**: [具体描述]
- **影响范围**: [对实践的影响]
- **相关任务**: [关联的任务/Issue]
- **优先级**: High/Medium/Low
- **状态**: 待研究 / 研究中 / 已解决

### 问题-002: ...

---

## 已解决问题

[链接到 resolved.md 或直接记录]

---

## 问题统计

| 类别 | 待研究 | 研究中 | 已解决 |
|------|--------|--------|--------|
| Agent交互 | X | X | X |
| 文档设计 | X | X | X |
| Token管理 | X | X | X |
| ... | | | |
```

### 2. issues/practice-related.md 格式

```markdown
# 实践层问题

> 📋 本项目特有的问题，由PM Agent处理

**维护者**: PM Agent

---

## 待处理问题

### 问题-XXX: [问题标题]

- **类型**: 技术问题 / 流程问题 / 协调问题
- **状态**: 待处理 / 处理中 / 已解决
- **负责人**: [Agent名称]
- **解决方案**: [处理方案]
```

### 3. Agent经验总结格式

每个Agent完成任务后，在 `knowledge-base/experiences/<agent>/` 下记录：

```markdown
# [任务名称] - 经验总结

**日期**: YYYY-MM-DD
**Agent**: [名称]
**任务**: [任务描述]

---

## 遇到的问题

1. 问题A
   - 原因: ...
   - 解决: ...
   - 是否框架相关: 是/否

2. 问题B
   - ...

---

## 有效做法

- 做法1: ...
- 做法2: ...

---

## 无效做法

- 做法1: ...
- 原因: ...

---

## 改进建议

- 对框架的建议: ...（会传递给Research Agent）
- 对实践的建议: ...
```

---

## 🔄 工作流程

### 日常流程

```
1. Agent工作过程中发现问题
   ↓
2. Agent记录到个人经验文档 (knowledge-base/experiences/<agent>/)
   ↓
3. Agent通知PM（通过状态更新或直接报告）
   ↓
4. PM读取问题，判断类型：
   - 框架相关 → 写入 issues/framework-related.md
   - 实践相关 → 写入 issues/practice-related.md
   ↓
5. PM定期（每周/每个Sprint结束）向用户汇报问题汇总
```

### Research Agent获取流程

```
1. Research Agent启动时
   ↓
2. 读取 practice/issues/framework-related.md
   ↓
3. 识别有价值的框架问题
   ↓
4. 开展研究，产出文档
   ↓
5. 更新问题状态，反馈研究结果
```

---

## 📋 PM Agent 职责清单

### 必须做的事

- [ ] 创建 `practice/issues/` 目录和相关文件
- [ ] 在各Agent的 CATCH_UP.md 或 ESSENTIALS.md 中添加问题报告指引
- [ ] 定期检查各Agent的经验文档
- [ ] 维护 `framework-related.md` 和 `practice-related.md`
- [ ] 向用户汇报问题汇总

### 问题分类标准

**框架相关问题**（写入 framework-related.md）：
- Agent交互模式的问题
- 文档体系设计的问题
- Context管理的问题
- Token-Based管理的问题
- 边界隔离机制的问题
- 方法论层面的问题

**实践相关问题**（写入 practice-related.md）：
- 具体技术实现问题
- 项目特定问题
- Agent个人能力问题
- 工具使用问题

---

## 🔗 与Research Agent的协作

### Research Agent会做什么

1. **定期读取** `practice/issues/framework-related.md`
2. **研究问题**，产出框架文档
3. **反馈结果**，更新问题状态

### PM需要通知Research Agent的情况

当发现**重要框架问题**时，可以通过以下方式通知Research Agent：
- 在 `framework-related.md` 中标记高优先级
- 让用户直接启动Research Agent讨论

---

## 📝 需要更新的Agent文档

### PM Agent 文档更新

1. **CATCH_UP.md** - 添加问题收集职责
2. **ESSENTIALS.md** - 添加详细的问题处理流程

### 其他 Agent 文档更新

在 **CATCH_UP.md** 或 **ESSENTIALS.md** 中添加：

```markdown
## 问题报告

工作过程中发现问题，请：

1. 记录到 `practice/knowledge-base/experiences/<agent>/[任务名].md`
2. 标明是否为框架相关问题
3. 通知PM Agent

框架相关问题示例：
- Agent交互不顺畅
- 文档格式不清晰
- Context信息过多/过少
- 模块边界不明确
```

---

## ✅ 执行检查清单

完成以下任务后，本机制即可运行：

### 目录创建
- [ ] 创建 `practice/issues/` 目录
- [ ] 创建 `practice/issues/README.md`
- [ ] 创建 `practice/issues/framework-related.md`
- [ ] 创建 `practice/issues/practice-related.md`
- [ ] 创建 `practice/issues/resolved.md`

### 文档更新
- [ ] 更新 PM Agent 的 CATCH_UP.md
- [ ] 更新 PM Agent 的 ESSENTIALS.md
- [ ] 更新 Data Agent 的文档
- [ ] 更新 Template Agent 的文档
- [ ] 更新 Test Agent 的文档

### 流程启动
- [ ] 向各Agent说明新的问题报告机制
- [ ] 在下一次任务中试行

---

**设计者**: Research Agent  
**日期**: 2026-03-06
