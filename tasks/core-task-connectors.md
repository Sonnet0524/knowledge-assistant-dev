# Core Team任务：Calendar 和 Notes 连接器

## 📋 任务背景

v1.2 Sprint 1 需要实现 Calendar 和 Notes 连接器，扩展数据源支持。

## 🎯 任务列表

### TASK-C2: Calendar Connector (Issue #38)

**优先级**: P1
**预计时间**: 3天

**任务要求**:
1. 创建 `scripts/connectors/calendar.py`
2. 实现 Google Calendar API 支持
3. 实现 iCal 文件解析
4. 实现按关键词/日期搜索事件
5. 编写单元测试

**API 示例**:
```python
from scripts.connectors.calendar import CalendarConnector

connector = CalendarConnector(provider="google")
events = connector.search_events("meeting", date_range=("2026-03-01", "2026-03-31"))
```

### TASK-C3: Notes Connector (Issue #39)

**优先级**: P1
**预计时间**: 3天

**任务要求**:
1. 创建 `scripts/connectors/notes.py`
2. 实现 Apple Notes 支持 (macOS)
3. 实现 Notion API 支持
4. 实现按内容搜索笔记
5. 编写单元测试

**API 示例**:
```python
from scripts.connectors.notes import NotesConnector

connector = NotesConnector(provider="notion")
notes = connector.search_notes("project")
```

## 📁 相关文件

参考已有的连接器框架:
- `scripts/connectors/base.py` - 基类
- `scripts/connectors/config.py` - 配置
- `scripts/connectors/registry.py` - 注册
- `scripts/connectors/email.py` - 示例实现

## ⚠️ 注意事项

1. 继承 BaseConnector 基类
2. 使用 ConnectorConfig 配置
3. 实现健康检查和重试逻辑
4. 测试覆盖率 > 80%

## 📤 输出要求

完成后在 `reports/core-report-connectors.md` 写入报告。

---
**创建者**: PM Team
**创建时间**: 2026-03-08
