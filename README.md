<p align="center">
  <img src="assets/TauricResearch.png" style="width: 60%; height: auto;">
</p>

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2412.20138" target="_blank"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2412.20138-B31B1B?logo=arxiv"/></a>
  <a href="https://discord.com/invite/hk9PGKShPK" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-TradingResearch-7289da?logo=discord&logoColor=white&color=7289da"/></a>
  <a href="./assets/wechat.png" target="_blank"><img alt="WeChat" src="https://img.shields.io/badge/WeChat-TauricResearch-brightgreen?logo=wechat&logoColor=white"/></a>
  <a href="https://x.com/TauricResearch" target="_blank"><img alt="X Follow" src="https://img.shields.io/badge/X-TauricResearch-white?logo=x&logoColor=white"/></a>
  <br>
  <a href="https://github.com/TauricResearch/" target="_blank"><img alt="Community" src="https://img.shields.io/badge/Join_GitHub_Community-TauricResearch-14C290?logo=discourse"/></a>
</div>

<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=de">Deutsch</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=es">Español</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=fr">français</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ja">日本語</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ko">한국어</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=pt">Português</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ru">Русский</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=zh">中文</a>
</div>

---

# TradingAgents: Multi-Agents LLM Financial Trading Framework 

> 🎉 **TradingAgents** officially released! We have received numerous inquiries about the work, and we would like to express our thanks for the enthusiasm in our community.
>
> So we decided to fully open-source the framework. Looking forward to building impactful projects with you!

<div align="center">
<a href="https://www.star-history.com/#TauricResearch/TradingAgents&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" />
   <img alt="TradingAgents Star History" src="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" style="width: 80%; height: auto;" />
 </picture>
</a>
</div>

<div align="center">

🚀 [TradingAgents](#tradingagents-framework) | ⚡ [Installation & CLI](#installation-and-cli) | 🎬 [Demo](https://www.youtube.com/watch?v=90gr5lwjIho) | 📦 [Package Usage](#tradingagents-package) | 🚀 [Deployment](#deployment) | 🤝 [Contributing](#contributing) | 📄 [Citation](#citation)

</div>

## Table of Contents

- [TradingAgents Framework](#tradingagents-framework)
- [Installation and CLI](#installation-and-cli)
- [TradingAgents Package](#tradingagents-package)
- [Deployment](#deployment)
  - [Docker Deployment](#docker-deployment)
  - [Feishu Bot Integration](#feishu-bot-integration)
  - [Custom API Server Configuration](#custom-api-server-configuration)
- [Contributing](#contributing)
- [Citation](#citation)

## TradingAgents Framework

TradingAgents is a multi-agent trading framework that mirrors the dynamics of real-world trading firms. By deploying specialized LLM-powered agents: from fundamental analysts, sentiment experts, and technical analysts, to trader, risk management team, the platform collaboratively evaluates market conditions and informs trading decisions. Moreover, these agents engage in dynamic discussions to pinpoint the optimal strategy.

<p align="center">
  <img src="assets/schema.png" style="width: 100%; height: auto;">
</p>

> TradingAgents framework is designed for research purposes. Trading performance may vary based on many factors, including the chosen backbone language models, model temperature, trading periods, the quality of data, and other non-deterministic factors. [It is not intended as financial, investment, or trading advice.](https://tauric.ai/disclaimer/)

Our framework decomposes complex trading tasks into specialized roles. This ensures the system achieves a robust, scalable approach to market analysis and decision-making.

### Analyst Team
- Fundamentals Analyst: Evaluates company financials and performance metrics, identifying intrinsic values and potential red flags.
- Sentiment Analyst: Analyzes social media and public sentiment using sentiment scoring algorithms to gauge short-term market mood.
- News Analyst: Monitors global news and macroeconomic indicators, interpreting the impact of events on market conditions.
- Technical Analyst: Utilizes technical indicators (like MACD and RSI) to detect trading patterns and forecast price movements.

<p align="center">
  <img src="assets/analyst.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

### Researcher Team
- Comprises both bullish and bearish researchers who critically assess the insights provided by the Analyst Team. Through structured debates, they balance potential gains against inherent risks.

<p align="center">
  <img src="assets/researcher.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### Trader Agent
- Composes reports from the analysts and researchers to make informed trading decisions. It determines the timing and magnitude of trades based on comprehensive market insights.

<p align="center">
  <img src="assets/trader.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### Risk Management and Portfolio Manager
- Continuously evaluates portfolio risk by assessing market volatility, liquidity, and other risk factors. The risk management team evaluates and adjusts trading strategies, providing assessment reports to the Portfolio Manager for final decision.
- The Portfolio Manager approves/rejects the transaction proposal. If approved, the order will be sent to the simulated exchange and executed.

<p align="center">
  <img src="assets/risk.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

## Installation and CLI

### Installation

Clone TradingAgents:
```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
```

Create a virtual environment in any of your favorite environment managers:
```bash
conda create -n tradingagents python=3.13
conda activate tradingagents
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Required APIs

You will also need the FinnHub API for financial data. All of our code is implemented with the free tier.
```bash
export FINNHUB_API_KEY=$YOUR_FINNHUB_API_KEY
```

You will need the OpenAI API for all the agents.
```bash
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY
```

### CLI Usage

You can also try out the CLI directly by running:
```bash
python -m cli.main
```
You will see a screen where you can select your desired tickers, date, LLMs, research depth, etc.

<p align="center">
  <img src="assets/cli/cli_init.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

An interface will appear showing results as they load, letting you track the agent's progress as it runs.

<p align="center">
  <img src="assets/cli/cli_news.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

<p align="center">
  <img src="assets/cli/cli_transaction.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

## TradingAgents Package

### Implementation Details

We built TradingAgents with LangGraph to ensure flexibility and modularity. We utilize `o1-preview` and `gpt-4o` as our deep thinking and fast thinking LLMs for our experiments. However, for testing purposes, we recommend you use `o4-mini` and `gpt-4.1-mini` to save on costs as our framework makes **lots of** API calls.

### Python Usage

To use TradingAgents inside your code, you can import the `tradingagents` module and initialize a `TradingAgentsGraph()` object. The `.propagate()` function will return a decision. You can run `main.py`, here's also a quick example:

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

You can also adjust the default configuration to set your own choice of LLMs, debate rounds, etc.

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-4.1-nano"  # Use a different model
config["quick_think_llm"] = "gpt-4.1-nano"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True # Use online tools or cached data

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

> For `online_tools`, we recommend enabling them for experimentation, as they provide access to real-time data. The agents' offline tools rely on cached data from our **Tauric TradingDB**, a curated dataset we use for backtesting. We're currently in the process of refining this dataset, and we plan to release it soon alongside our upcoming projects. Stay tuned!

You can view the full list of configurations in `tradingagents/default_config.py`.

## Deployment

TradingAgents supports various deployment methods, including Docker containerization, Feishu bot integration for notifications, and custom self-hosted OpenAI-compatible API servers.

### Docker Deployment

The project includes a complete Docker deployment setup with automated scheduling for daily trading analysis.

#### Prerequisites

1. **Create Environment File**
   ```bash
   cp .env.example .env
   ```

2. **Configure Environment Variables**
   Edit `.env` file with your API keys and settings:
   ```bash
   # Required API Keys
   OPENAI_API_KEY=your_openai_api_key_here
   FINNHUB_API_KEY=your_finnhub_api_key_here
   
   # Custom OpenAI-compatible API Server (optional)
   OPENAI_API_BASE=https://your-custom-api-server.com/v1
   
   # Feishu Bot Integration (optional)
   FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-token
   
   # Trading Configuration
   STOCK_SYMBOLS=AAPL,MSFT,GOOGL,TSLA,NVDA
   ANALYSIS_TIME=14:30  # UTC time for daily analysis
   ```

#### Quick Start

1. **Build and Run**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. **Check Service Status**
   ```bash
   docker-compose ps
   docker-compose logs -f tradingagents
   ```

#### Manual Deployment

1. **Build Docker Image**
   ```bash
   docker-compose build
   ```

2. **Start Services**
   ```bash
   docker-compose up -d
   ```

3. **View Logs**
   ```bash
   docker-compose logs -f
   ```

#### Configuration Files

- `docker-compose.yml`: Docker services configuration
- `Dockerfile`: Container build instructions
- `trading_service.py`: Automated trading analysis service
- `deploy.sh`: One-click deployment script

### Feishu Bot Integration

TradingAgents supports integration with Feishu (飞书) bot for real-time notifications of trading results and error alerts.

#### Setup Feishu Bot

1. **Create Feishu Bot**
   - Go to Feishu group settings
   - Add a custom bot
   - Set custom keyword trigger to: **"BMD"** (Bot Market Data)
   - Copy the webhook URL

2. **Configure Webhook**
   ```bash
   export FEISHU_WEBHOOK_URL="https://open.feishu.cn/open-apis/bot/v2/hook/your-webhook-token"
   ```

3. **Bot Features**
   - **Daily Analysis Reports**: Automatically sends trading analysis results
   - **Error Notifications**: Alerts for system errors or API failures
   - **Custom Keyword**: All messages include "BMD" keyword for proper routing
   - **Rich Formatting**: Supports markdown and interactive cards

#### Message Types

- **Success Notifications**: Trading analysis results with recommendations
- **Error Alerts**: System failures, API errors, or configuration issues
- **Status Updates**: Service health and operational status

For detailed Feishu bot setup instructions, see [FEISHU_SETUP.md](FEISHU_SETUP.md).

### Custom API Server Configuration

TradingAgents supports custom self-hosted OpenAI-compatible API servers for enhanced privacy and cost control.

#### Supported API Servers

- **Official OpenAI API**: Default configuration
- **Self-hosted servers**: Compatible with OpenAI API format
- **Cloud providers**: Azure OpenAI, AWS Bedrock (with compatibility layers)
- **Local deployments**: Ollama, vLLM, LocalAI

#### Configuration

1. **Set Custom API Base**
   ```bash
   export OPENAI_API_BASE="https://your-custom-server.com/v1"
   export OPENAI_API_KEY="your-custom-api-key"
   ```

2. **Verify Connection**
   ```bash
   python scripts/test_custom_api.py
   ```

3. **Configure Model Names**
   Update `tradingagents/default_config.py`:
   ```python
   # Custom model names for your API server
   "deep_think_llm": "your-model-name",
   "quick_think_llm": "your-fast-model-name",
   ```

#### API Compatibility

- **Required endpoints**: `/chat/completions`
- **Optional endpoints**: `/embeddings`, `/models`
- **Supported features**: Streaming, function calling, temperature control

For detailed API server setup instructions, see [CUSTOM_API_SETUP.md](CUSTOM_API_SETUP.md) and [API_CONFIG_README.md](API_CONFIG_README.md).

#### Troubleshooting

1. **Test API Connection**
   ```bash
   python scripts/validate_api_config.py
   ```

2. **Check Docker Logs**
   ```bash
   docker-compose logs tradingagents
   ```

3. **Verify Environment Variables**
   ```bash
   docker-compose exec tradingagents env | grep -E "(OPENAI|FINNHUB|FEISHU)"
   ```

#### Service Management

- **Restart Service**: `docker-compose restart tradingagents`
- **Update Configuration**: Edit `.env` and restart
- **View Results**: Check `results/` directory
- **Monitor Logs**: Check `logs/` directory

## Contributing

We welcome contributions from the community! Whether it's fixing a bug, improving documentation, or suggesting a new feature, your input helps make this project better. If you are interested in this line of research, please consider joining our open-source financial AI research community [Tauric Research](https://tauric.ai/).

## Citation

Please reference our work if you find *TradingAgents* provides you with some help :)

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework}, 
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138}, 
}
```
