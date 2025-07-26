# 自建OpenAI API服务器配置指南

TradingAgents现在支持使用自建的OpenAI兼容API服务器，包括但不限于：

- 自部署的OpenAI API代理
- vLLM服务器
- Ollama
- LocalAI
- FastChat
- 其他OpenAI兼容的API服务

## 1. 基本配置

在 `.env` 文件中设置以下环境变量：

```bash
# 自建API服务器配置
OPENAI_API_KEY=your_custom_api_key
OPENAI_BASE_URL=http://your-server:port/v1

# 或使用通用配置
API_KEY=your_custom_api_key
LLM_PROVIDER=openai

# 模型配置
DEEP_THINK_LLM=your_model_name
QUICK_THINK_LLM=your_model_name
```

## 2. 常见自建服务配置示例

### vLLM服务器

```bash
# vLLM服务器配置示例
OPENAI_API_KEY=EMPTY
OPENAI_BASE_URL=http://localhost:8000/v1
DEEP_THINK_LLM=meta-llama/Llama-2-70b-chat-hf
QUICK_THINK_LLM=meta-llama/Llama-2-13b-chat-hf
```

### Ollama本地服务

```bash
# Ollama配置示例
OPENAI_API_KEY=ollama
OPENAI_BASE_URL=http://localhost:11434/v1
DEEP_THINK_LLM=llama3.1:70b
QUICK_THINK_LLM=llama3.1:8b
```

### LocalAI

```bash
# LocalAI配置示例
OPENAI_API_KEY=your_localai_key
OPENAI_BASE_URL=http://localhost:8080/v1
DEEP_THINK_LLM=gpt-4
QUICK_THINK_LLM=gpt-3.5-turbo
```

### 自部署的OpenAI代理

```bash
# OpenAI代理服务器
OPENAI_API_KEY=sk-your-proxy-key
OPENAI_BASE_URL=https://your-proxy-domain.com/v1
DEEP_THINK_LLM=gpt-4o
QUICK_THINK_LLM=gpt-4o-mini
```

## 3. 支持的LLM提供商

### OpenAI兼容服务 (推荐)

```bash
LLM_PROVIDER=openai
OPENAI_BASE_URL=your_custom_endpoint
```

### Anthropic Claude

```bash
LLM_PROVIDER=anthropic
API_KEY=your_anthropic_key
DEEP_THINK_LLM=claude-3-opus-20240229
QUICK_THINK_LLM=claude-3-sonnet-20240229
```

### Google Gemini

```bash
LLM_PROVIDER=google
API_KEY=your_google_api_key
DEEP_THINK_LLM=gemini-1.5-pro
QUICK_THINK_LLM=gemini-1.5-flash
```

## 4. 部署和测试

### 4.1 部署服务

```bash
# 配置环境变量
cp .env.example .env
# 编辑 .env 文件

# 部署服务
./deploy.sh
```

### 4.2 测试API连接

```bash
# 测试单只股票分析
docker-compose exec tradingagents python trading_service.py test AAPL

# 查看LLM配置
docker-compose exec tradingagents python -c "
from tradingagents.default_config import DEFAULT_CONFIG
config = DEFAULT_CONFIG.copy()
print('Provider:', config['llm_provider'])
print('API Endpoint:', config['backend_url'])
print('Deep Model:', config['deep_think_llm'])
print('Quick Model:', config['quick_think_llm'])
"
```

## 5. 性能优化建议

### 5.1 模型选择

- **深度思考模型**: 用于复杂分析，建议使用更强的模型
- **快速思考模型**: 用于简单任务，可以使用较小的模型

```bash
# 平衡性能和成本的配置
DEEP_THINK_LLM=gpt-4o-mini  # 或您的大模型
QUICK_THINK_LLM=gpt-4o-mini  # 或您的小模型
```

### 5.2 减少API调用

```bash
# 减少debate轮数以降低API调用
MAX_DEBATE_ROUNDS=1
MAX_RISK_DISCUSS_ROUNDS=1

# 选择性启用分析师
# 在代码中可以指定: selected_analysts=["market", "news"]
```

## 6. 故障排除

### 6.1 连接问题

1. **检查网络连接**
   ```bash
   curl -X GET "http://your-server:port/v1/models" \
        -H "Authorization: Bearer your_api_key"
   ```

2. **检查API密钥**
   - 确保API密钥格式正确
   - 检查密钥是否有效

3. **检查模型名称**
   - 确认模型名称在服务器上可用
   - 检查模型是否已加载

### 6.2 常见错误

- **401 Unauthorized**: API密钥错误
- **404 Not Found**: 端点地址错误或模型不存在
- **500 Internal Server Error**: 服务器内部错误
- **Connection Error**: 网络连接问题

### 6.3 日志查看

```bash
# 查看服务日志
docker-compose logs -f tradingagents

# 查看特定时间的日志
docker-compose logs --since="1h" tradingagents
```

## 7. 安全建议

1. **API密钥安全**
   - 不要在代码中硬编码API密钥
   - 使用环境变量管理敏感信息
   - 定期轮换API密钥

2. **网络安全**
   - 在生产环境中使用HTTPS
   - 配置防火墙规则
   - 限制API访问来源

3. **访问控制**
   - 设置适当的API访问权限
   - 监控API使用情况
   - 设置访问频率限制

## 8. 高级配置

### 8.1 多服务器负载均衡

可以通过代理服务器实现多个API端点的负载均衡：

```bash
OPENAI_BASE_URL=http://your-load-balancer:port/v1
```

### 8.2 模型热切换

通过环境变量实现不同场景下的模型切换：

```bash
# 开发环境 - 使用较小模型
DEEP_THINK_LLM=gpt-3.5-turbo
QUICK_THINK_LLM=gpt-3.5-turbo

# 生产环境 - 使用更强模型
DEEP_THINK_LLM=gpt-4o
QUICK_THINK_LLM=gpt-4o-mini
```

---

通过以上配置，您可以轻松地将TradingAgents连接到任何OpenAI兼容的API服务器！
