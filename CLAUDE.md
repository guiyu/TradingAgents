# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

TradingAgents 是一个基于多智能体的金融交易框架，模拟真实交易公司的团队协作流程。系统包含五个主要团队：分析师团队、研究团队、交易团队、风险管理团队和投资组合管理团队，通过 LLM 驱动的智能体协作完成投资决策。

## 核心架构

### 智能体组织结构
```
分析师团队 → 研究团队 → 交易团队 → 风险管理团队 → 投资组合管理团队
```

- **Analyst Team**: 基础分析（市场、新闻、情感、基本面）
- **Research Team**: 多空辩论（看涨研究员、看跌研究员、研究经理）
- **Trader**: 基于分析制定交易计划
- **Risk Management**: 风险评估（激进、保守、中性分析师）
- **Portfolio Manager**: 最终交易决策

### 关键模块
- `tradingagents/graph/`: LangGraph 核心图结构和流程控制
- `tradingagents/agents/`: 各类智能体实现
- `tradingagents/dataflows/`: 数据获取和处理工具
- `cli/`: 命令行交互界面

## 开发工作流

### 安装和环境设置

#### 方法1：使用Conda（推荐）
```bash
# 创建虚拟环境
conda create -n tradingagents python=3.13
conda activate tradingagents

# 安装依赖
pip install -r requirements.txt
```

#### 方法2：使用Python venv
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

#### 必需的环境变量
```bash
# 必需的API密钥
export FINNHUB_API_KEY=$YOUR_FINNHUB_API_KEY
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY

# 可选的其他LLM提供商密钥
export ANTHROPIC_API_KEY=$YOUR_ANTHROPIC_API_KEY
export GOOGLE_API_KEY=$YOUR_GOOGLE_API_KEY
```

#### 环境检查
使用提供的环境检查脚本验证设置：
```bash
# 在虚拟环境中运行
source venv/bin/activate
python3 check_env.py
```

#### 常见问题解决

**问题1**: `ModuleNotFoundError: No module named 'langchain_openai'`
- **解决**: 确保在虚拟环境中运行 `pip install -r requirements.txt`

**问题2**: `OpenAIError: The api_key client option must be set`
- **解决**: 设置环境变量 `export OPENAI_API_KEY=$YOUR_API_KEY`

**问题3**: `externally-managed-environment` 错误
- **解决**: 使用虚拟环境而非系统Python安装依赖

**问题4**: API密钥管理
- **解决**: 复制 `.env.example` 为 `.env` 并填入密钥，或直接设置环境变量

### 运行命令

#### 快速启动（推荐）
使用提供的启动脚本，自动处理虚拟环境和依赖：
```bash
# 检查环境和运行主脚本
./start.sh python main.py

# 检查环境和运行CLI
./start.sh python -m cli.main

# 只检查环境（不运行程序）
./start.sh
```

#### 使用 CLI
```bash
# 运行交互式 CLI
python -m cli.main

# 直接分析（使用 typer 命令）
python -m cli.main analyze
```

#### 程序化使用
```bash
# 运行主脚本
python main.py

# 自定义配置运行
# 修改 main.py 中的配置参数后运行
```

### 配置管理

#### 核心配置文件
- `tradingagents/default_config.py`: 默认配置参数
- `main.py`: 自定义配置示例

#### 重要配置项
```python
config = {
    "llm_provider": "openai|google|anthropic",  # LLM 提供商
    "deep_think_llm": "o4-mini",               # 深度思考模型
    "quick_think_llm": "gpt-4o-mini",          # 快速思考模型
    "max_debate_rounds": 1,                    # 辩论轮数
    "online_tools": True,                      # 是否使用在线工具
}
```

## 开发指南

### 添加新智能体
1. 在相应的 `tradingagents/agents/` 子目录下创建智能体类
2. 继承适当的基类并实现必要的方法
3. 在图结构中注册新智能体

### 集成新数据源
1. 在 `tradingagents/dataflows/` 中创建新的工具模块
2. 实现数据获取和处理逻辑
3. 在相关智能体中集成新工具

### 修改决策流程
- 主要流程控制在 `tradingagents/graph/` 模块中
- 使用 LangGraph 定义状态转换和条件逻辑
- 修改 `trading_graph.py` 中的图结构

### 测试和调试
```bash
# 启用调试模式
ta = TradingAgentsGraph(debug=True, config=config)

# 结果输出目录
# 默认: ./results/{ticker}/{date}/
```

## 文件结构要点

### 状态管理
- `AgentState`: 智能体间共享状态
- `InvestDebateState`: 投资辩论状态
- `RiskDebateState`: 风险评估辩论状态

### 内存系统
- `FinancialSituationMemory`: 金融情况记忆管理
- 支持反思和学习机制

### CLI 界面
- Rich 库驱动的实时状态显示
- 分组展示各团队智能体进度
- 实时报告更新和消息流

## API 密钥和安全

项目需要以下 API 服务：
- FinnHub API（金融数据）
- OpenAI API（主要 LLM 提供商）
- 可选：Google Gemini、Anthropic Claude、NewAPI

### 支持的 LLM 提供商

#### 1. OpenAI
```bash
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY
```

#### 2. NewAPI 平台
NewAPI 是一个统一的 API 管理平台，支持多个 AI 模型：
```bash
# 设置 NewAPI 密钥（使用 OPENAI_API_KEY 环境变量）
export OPENAI_API_KEY=$YOUR_NEWAPI_KEY
```

**支持的模型类型：**
- **国际模型**: GPT-4o, GPT-3.5-turbo, Claude-3.5-sonnet, Gemini-pro
- **中国模型**: DeepSeek-chat, GLM-4-flash, Qwen-turbo, ERNIE-4.0, Spark-Max
- **专业模型**: DeepSeek-coder (代码专用), GPT-4-turbo (推理增强)

**配置示例：**
```python
config = {
    "llm_provider": "newapi",
    "backend_url": "https://b4u.qzz.io/v1",
    "deep_think_llm": "gpt-4o",
    "quick_think_llm": "gpt-4o-mini",
}
```

#### 3. 其他提供商
- Anthropic Claude、Google Gemini、OpenRouter、Ollama（本地）

### 使用建议

- **成本优化**: 使用 NewAPI 的中国模型（DeepSeek、GLM-4）可显著降低成本
- **性能平衡**: 深度思考用高性能模型，快速思考用轻量模型
- **模型选择**: 根据任务复杂度选择合适的模型组合

确保敏感信息通过环境变量设置，避免硬编码在代码中。