# TradingAgents API配置指南

TradingAgents 现已支持多种 API 配置方式，包括官方 OpenAI API 和自建的兼容服务器。

## 🎯 快速开始

### 1. 复制配置模板
```bash
cp .env.example .env
```

### 2. 编辑配置文件
根据您的需求选择以下配置方式之一：

#### 官方 OpenAI API
```bash
OPENAI_API_KEY=sk-your-official-openai-key
OPENAI_BASE_URL=https://api.openai.com/v1
DEEP_THINK_LLM=gpt-4o
QUICK_THINK_LLM=gpt-4o-mini
```

#### 自建 API 服务器
```bash
OPENAI_API_KEY=your-custom-api-key
OPENAI_BASE_URL=http://your-server:8000/v1
DEEP_THINK_LLM=your-model-name
QUICK_THINK_LLM=your-model-name
```

### 3. 配置金融数据 API
```bash
FINNHUB_API_KEY=your-finnhub-key  # 免费注册: https://finnhub.io
```

### 4. 配置飞书机器人（可选）
```bash
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/your-token
```

## 🔧 支持的配置选项

### 核心配置
| 环境变量 | 描述 | 默认值 | 示例 |
|---------|------|--------|------|
| `OPENAI_API_KEY` | API密钥 | 必需 | `sk-...` |
| `OPENAI_BASE_URL` | API服务器地址 | `https://api.openai.com/v1` | `http://localhost:8000/v1` |
| `LLM_PROVIDER` | LLM提供商 | `openai` | `openai`, `anthropic`, `google` |
| `DEEP_THINK_LLM` | 深度思考模型 | `gpt-4o-mini` | `gpt-4o`, `claude-3-opus` |
| `QUICK_THINK_LLM` | 快速思考模型 | `gpt-4o-mini` | `gpt-4o-mini`, `claude-3-sonnet` |

### 功能配置
| 环境变量 | 描述 | 默认值 |
|---------|------|--------|
| `MAX_DEBATE_ROUNDS` | 辩论轮数 | `1` |
| `ONLINE_TOOLS` | 启用在线工具 | `true` |
| `TRADING_TICKERS` | 监控股票列表 | `AAPL,MSFT,GOOGL,TSLA,NVDA` |

## 🚀 快速部署

### 方法1: 一键部署
```bash
./deploy.sh
```

### 方法2: 手动部署
```bash
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d

# 查看状态
docker-compose ps
```

## 🧪 测试配置

### 运行配置测试
```bash
python test_api_config.py
```

### 测试单只股票分析
```bash
# 在容器内测试
docker-compose exec tradingagents python trading_service.py test AAPL

# 或直接运行
python trading_service.py test AAPL
```

## 🛠️ 自建API服务器支持

TradingAgents 支持各种 OpenAI 兼容的 API 服务：

### vLLM
```bash
OPENAI_API_KEY=EMPTY
OPENAI_BASE_URL=http://localhost:8000/v1
DEEP_THINK_LLM=meta-llama/Llama-2-70b-chat-hf
```

### Ollama
```bash
OPENAI_API_KEY=ollama
OPENAI_BASE_URL=http://localhost:11434/v1
DEEP_THINK_LLM=llama3.1:70b
```

### LocalAI
```bash
OPENAI_API_KEY=your-localai-key
OPENAI_BASE_URL=http://localhost:8080/v1
DEEP_THINK_LLM=gpt-4
```

详细配置请参考 [CUSTOM_API_SETUP.md](CUSTOM_API_SETUP.md)

## 📱 飞书机器人集成

1. **创建飞书机器人**
   - 在飞书群中添加自定义机器人
   - 获取 Webhook URL

2. **配置环境变量**
   ```bash
   FEISHU_WEBHOOK_URL=your-webhook-url
   ```

3. **测试机器人**
   ```bash
   docker-compose exec tradingagents python trading_service.py test AAPL
   ```

详细设置请参考 [FEISHU_SETUP.md](FEISHU_SETUP.md)

## 🔍 常用命令

### 服务管理
```bash
# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f tradingagents

# 重启服务
docker-compose restart

# 停止服务
docker-compose down
```

### 分析操作
```bash
# 测试单只股票
docker-compose exec tradingagents python trading_service.py test AAPL

# 运行完整分析
docker-compose exec tradingagents python trading_service.py once

# 查看配置信息
docker-compose exec tradingagents python -c "
from tradingagents.default_config import DEFAULT_CONFIG
import json
print(json.dumps(DEFAULT_CONFIG, indent=2))
"
```

## 🔧 故障排除

### API连接问题
1. **检查API密钥**: 确保密钥格式正确且有效
2. **检查服务器地址**: 确认地址可访问
3. **检查模型名称**: 确认模型在服务器上可用

### 常见错误
- `401 Unauthorized`: API密钥错误
- `404 Not Found`: 端点或模型不存在
- `Connection Error`: 网络连接问题

### 调试方法
```bash
# 运行配置测试
python test_api_config.py

# 查看详细日志
docker-compose logs tradingagents

# 检查环境变量
docker-compose exec tradingagents env | grep -E "(OPENAI|API|LLM)"
```

## 💡 性能优化建议

### 降低成本
```bash
# 使用较小的模型
DEEP_THINK_LLM=gpt-4o-mini
QUICK_THINK_LLM=gpt-4o-mini

# 减少辩论轮数
MAX_DEBATE_ROUNDS=1
MAX_RISK_DISCUSS_ROUNDS=1
```

### 提高准确性
```bash
# 使用更强的模型
DEEP_THINK_LLM=gpt-4o
QUICK_THINK_LLM=gpt-4o-mini

# 增加辩论轮数
MAX_DEBATE_ROUNDS=2
MAX_RISK_DISCUSS_ROUNDS=2
```

## 📚 相关文档

- [自建API服务器配置](CUSTOM_API_SETUP.md)
- [飞书机器人设置](FEISHU_SETUP.md)
- [Docker部署指南](README.md#installation-and-cli)

---

现在您可以使用任何OpenAI兼容的API服务来运行TradingAgents！🚀
