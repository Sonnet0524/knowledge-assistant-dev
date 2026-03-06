# Agent Team Framework

> 🤝 AI Agent协作模式研究成果

**性质**: 研究成果发布 | **版本**: v1.0 | **更新**: 2026-03-06

---

## 💡 一句话总结

探索**基于文档的Agent交互模式**，实现多Agent的高效、可自动化协作。

---

## 🎯 核心研究

### Agent交互模式 ⭐

**问题**: Agent之间如何高效、可靠地交互？

**成果**:
- 📄 文档化上下文交换机制
- 🔌 标准化交互协议
- 🚀 Message Queue自动化愿景

**效果**: 
- Context ↓93% | 冲突率 ↓100% | 预测准确率 ↑70%

📖 [深入研究](docs/research/agent-interaction/)

---

### 信息流架构 🔄

**问题**: "人-智能-基础能力"三层架构中，信息流如何优化？

**方向**:
- Agent First vs Human First
- 信息流性价比分析
- 动态平衡机制

📖 [探索研究](docs/research/information-architecture/)

---

### Token-Based管理 📊

**问题**: Token能否作为Agent工作量度量单位？

**状态**: 方法论提出，验证中

📖 [参与探讨](docs/research/token-based/)

---

## 📊 关键数据

| 指标 | 传统方式 | 本研究 | 改进 |
|------|---------|--------|------|
| Context使用 | 600行 | 40行 | ↓93% |
| 协作冲突 | 每周3次 | 0次 | ↓100% |
| 预测准确率 | 50% | 85% | ↑70% |
| 启动时间 | 5秒 | 1秒 | ↓80% |

---

## 🛠️ 实践验证

### Knowledge Assistant项目

- **规模**: 中型（55,000 tokens）
- **团队**: 4-Agent协作
- **验证**: Agent交互模式的有效性

📖 [查看实践](docs/practice/knowledge-assistant/)

---

## 📚 文档导航

### 快速入门

- 🎓 [研究概览](docs/) - 了解研究全貌
- 🔬 [核心研究](docs/research/agent-interaction/) - Agent交互模式
- 🛠️ [实践验证](docs/practice/knowledge-assistant/) - 验证项目

### 深入了解

- 📖 [方法论](docs/methodology/) - 文档分层、Context最小化等
- 📊 [经验教训](docs/practice/lessons-learned/) - 实践总结
- 🔍 [对比分析](docs/reference/comparison.md) - 与其他方法对比

### 未来方向

- 🚀 [研究方向](docs/reference/future-directions.md) - 短中长期规划

---

## 🤝 参与贡献

本研究欢迎：

- 💬 **理论探讨** - 对研究假设的建议
- 🧪 **实验验证** - 在其他场景中验证
- 🐛 **问题发现** - 实践中的问题
- 💡 **创新想法** - 新的研究方向

**参与方式**:
- [GitHub Discussions](https://github.com/Sonnet0524/knowledge-assistant-dev/discussions)
- [提交Issue](https://github.com/Sonnet0524/knowledge-assistant-dev/issues)

---

## 📖 引用

```bibtex
@misc{agent-team-framework-2026,
  title={Agent Team Framework: A Document-based Agent Interaction Model},
  author={Agent Team},
  year={2026},
  url={https://github.com/Sonnet0524/knowledge-assistant-dev}
}
```

---

## 📂 项目结构

```
├── docs/                   # 📚 研究成果文档
│   ├── research/           # 🔬 核心研究
│   ├── practice/           # 🛠️ 实践验证
│   ├── methodology/        # 📖 方法论
│   └── reference/          # 📚 参考资料
├── agents/                 # 🤖 Agent配置（项目执行）
├── project-management/     # 📊 项目管理
├── knowledge-base/         # 🧠 知识库
└── development-guide/      # 🔧 开发指南
```

---

**研究团队**: Agent Team  
**许可协议**: MIT License

---

**快速跳转**: [研究概览](docs/) | [Agent交互](docs/research/agent-interaction/) | [实践验证](docs/practice/knowledge-assistant/)

---

## 📜 许可协议

### 代码部分

本项目代码采用 **GNU Affero General Public License v3.0 (AGPL v3.0)** 协议开源。

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

**关键要求**：
- ✅ 自由使用、修改和分发
- ✅ 任何修改版本必须以AGPL开源
- ✅ 网络服务使用也必须开源（AGPL特有）
- ✅ 必须保留版权声明

**商业使用**：如需商业使用，请联系获取商业许可。

📄 [查看完整协议](LICENSE)

---

### 知识内容

本项目的文档、知识库等知识内容采用 **CC BY-NC-SA 4.0** 协议。

**关键要求**：
- ✅ 必须署名
- ❌ 禁止商业使用
- ✅ 相同方式共享

**商业使用**：如需商业使用，请联系获取商业许可。

📄 [查看完整协议](KNOWLEDGE_LICENSE)

---

## 🏷️ 版权声明

Copyright © 2026 Agent Team. All rights reserved.

本项目包括：
- 代码（AGPL v3.0）：允许开源使用，禁止闭源商业使用
- 知识（CC BY-NC-SA 4.0）：允许非商业使用，禁止商业使用

**商业合作**：通过 [GitHub Issues](https://github.com/Sonnet0524/knowledge-assistant-dev/issues) 联系
