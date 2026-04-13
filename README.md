## 🚀 迭代路径 (Milestones)

```
apt-get update && apt-get install -y libgl1 libglib2.0-0
```

我建议你按照以下三个阶段稳步推进，确保每个阶段都有可交付的成果：

### **Milestone 1: 数据管线与原子能力验证**
* **目标**：成功运行 Docling 解析，并打通本地向量存储。
* **关键动作**：
    * 配置基于 `uv` 的开发容器，挂载权重缓存目录。
    * 编写 Python 脚本，使用 **Docling** 将一个含有复杂表格和图片的 Docx 拆分为清晰的片段。
    * 在容器内成功运行 **Milvus Lite**（或连接宿主机 Docker 版 Milvus），实现片段的存入与初步检索。

### **Milestone 2: Agent 封装与工具集成**
* **目标**：将检索逻辑转化为 Agent 可用的“超能力”。
* **关键动作**：
    * 使用 **Pydantic AI** 定义系统依赖 `Deps`，实现 Milvus 客户端的单例管理。
    * 将检索逻辑封装为 `@agent.tool`，并在工具内部实现 **Hybrid Search**（向量 + 关键词）。
    * 测试 Agent 的“重写”能力：确保它能处理“那那个呢？”这种关联上下文的追问。

### **Milestone 3: 端到端交付与 UI 展示**
* **目标**：构建完整的客服 Demo，具备生产环境的雏形。
* **关键动作**：
    * 集成 **Chainlit** 前端，配置 `on_chat_start` 和 `on_message` 钩子调用 Pydantic AI。
    * 实现 **Streaming**（流式输出）和 **Step-wise**（步骤显示），让用户能看到 Agent 检索知识库的过程。
    * 完成 Docker Compose 的最终配置，实现一键拉起整个应用栈。