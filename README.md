🚀 LLM RAG + Agent Demo（基于 LangChain）

一个完整实现的 LLM 应用 Demo，包含 RAG 检索增强生成 + Tool Agent 调用机制
适用于大模型应用开发 / RAG 系统开发 / AI 工程方向

📌 项目背景

随着大模型应用的发展，单纯 Prompt 调用已经无法满足企业级场景需求。本项目围绕：

检索增强生成（RAG）

Tool 调用机制

Prompt 工程

向量数据库

Agent 多步推理

构建了一个完整的 LLM 应用基础架构 Demo。

该项目重点体现：

对 LLM 应用结构的系统理解

对 RAG 核心参数与召回机制的掌握

对 Agent 调用逻辑的实现能力

对 LangChain Runnable 架构的熟练使用

🏗️ 系统架构
  
  用户问题-->Retriever(VectorStore)-->拼接上下文 + Prompt-->LLM 
Agent 模块：

用户问题 → LLM 决策 → 是否调用 Tool → 工具执行 → 返回结果 → LLM 生成最终回答
🔧 技术栈
模块	技术
LLM 调用	LangChain
Embedding	OpenAI / DeepSeek 可替换
向量数据库	FAISS
文档处理	RecursiveCharacterTextSplitter
Agent	Tool + Pydantic Schema
Prompt 工程	PromptTemplate
Runnable 架构	LCEL
🧠 核心能力体现
1️⃣ RAG 系统完整实现

实现完整 Pipeline：

文档加载

语义切分（chunk_size + overlap）

Embedding 向量化

FAISS 向量索引

Top-K 检索

拼接上下文生成回答

🔍 重点优化理解

chunk_size 与 recall / 噪声 / token 成本权衡

overlap 对边界信息保护作用

metadata 设计用于来源追踪与可解释性

2️⃣ Agent + Tool 调用机制

实现：

Pydantic 定义工具参数 Schema

LLM 自动决策是否调用工具

JSON 格式工具调用

ReAct 思想实现

体现能力：

对函数调用原理的理解

对模型工具选择机制的掌握

对多步推理流程的控制

3️⃣ LangChain Runnable 架构掌握

使用 LCEL（LangChain Expression Language）构建链式调用：

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | chat_model
)

体现：

对数据流的抽象能力

对组件组合式设计的理解

对模块解耦的掌握

## 📂 项目结构
```text
Langchain/
│
├── toolagent.ipynb
│
├── ModelIO/
│   ├── prompt_template.ipynb
│   ├── chatmodel.ipynb
│   ├── llms.ipynb
│   └── output_parser.ipynb
│
└── RAG/
    ├── code.py
    ├── document_loaders.ipynb
    ├── text_splitter.ipynb
    └── sql.md
```
📈 可扩展方向

该项目设计为可扩展架构，可进一步升级为：

多轮对话记忆

混合检索（BM25 + 向量）

召回率评测模块

FastAPI 部署为在线服务

接入本地大模型（Qwen / DeepSeek）

引入 reranker 提升精度

增加 embedding 对比实验
