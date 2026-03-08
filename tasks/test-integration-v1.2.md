# Test Team任务：v1.2 集成测试

## 📋 任务背景

v1.2 所有开发任务已完成，需要进行最终集成测试验证。

## ⚠️ 重要：工作目录

**当前在 dev 仓库**，但测试需要在 main 仓库执行。

**切换到 main 仓库**:
```bash
cd ../knowledge-assistant
```

## 🎯 具体任务 - TASK-TE6: Integration Tests v1.2 (Issue #50)

**优先级**: P0

## 测试步骤

### 1. 切换到 main 仓库并运行测试
```bash
cd ../knowledge-assistant
pytest tests/ -v --cov=scripts --cov-report=term-missing
```

### 2. 验证核心功能

**在 main 仓库**运行:
```bash
cd ../knowledge-assistant

# 测试连接器
pytest tests/test_connector*.py -v

# 测试提取功能
pytest tests/test_extraction.py -v

# 测试API
pytest tests/test_api*.py -v

# 测试性能
pytest tests/test_performance.py -v
```

### 3. 检查测试覆盖率
```bash
cd ../knowledge-assistant
pytest --cov=scripts --cov-report=term
```

### 4. 汇总测试结果

统计:
- 总测试数
- 通过数
- 失败数
- 覆盖率

## 📤 输出要求

完成后在 `reports/test-integration-v1.2.md` 写入报告，包含：
1. 测试结果统计
2. 覆盖率数据
3. 各模块测试状态
4. 发布建议

---
**创建者**: PM Team
**创建时间**: 2026-03-08
