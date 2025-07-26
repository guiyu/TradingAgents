#!/bin/bash

# TradingAgents 部署脚本 - 支持自建API服务器

set -e

echo "🚀 开始部署 TradingAgents 服务..."

# 检查环境变量配置文件
if [ ! -f ".env" ]; then
    echo "⚠️  未找到 .env 文件，请先配置 API 密钥"
    echo "📝 复制 .env.example 到 .env 并填入您的 API 密钥:"
    echo "   cp .env.example .env"
    echo ""
    echo "🔧 支持的配置选项:"
    echo "   OPENAI_API_KEY - OpenAI API密钥"
    echo "   OPENAI_BASE_URL - 自建API服务器地址 (默认: https://api.openai.com/v1)"
    echo "   API_KEY - 通用API密钥 (可替代OPENAI_API_KEY)"
    echo "   LLM_PROVIDER - LLM提供商 (openai/anthropic/google)"
    echo "   DEEP_THINK_LLM - 深度思考模型名称"
    echo "   QUICK_THINK_LLM - 快速思考模型名称"
    echo "   FINNHUB_API_KEY - FinnHub金融数据API"
    echo "   FEISHU_WEBHOOK_URL - 飞书机器人Webhook"
    echo ""
    echo "💡 示例配置 (自建API服务器):"
    echo "   OPENAI_API_KEY=sk-your-custom-key"
    echo "   OPENAI_BASE_URL=http://your-server:8000/v1"
    echo "   DEEP_THINK_LLM=gpt-4"
    echo "   QUICK_THINK_LLM=gpt-3.5-turbo"
    exit 1
fi

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose 未安装，请先安装 Docker Compose"
    exit 1
fi

# 读取.env文件并显示配置信息
echo "📋 当前配置:"
if [ -f ".env" ]; then
    source .env
    echo "   LLM Provider: ${LLM_PROVIDER:-openai}"
    echo "   API Endpoint: ${OPENAI_BASE_URL:-https://api.openai.com/v1}"
    echo "   Deep Think Model: ${DEEP_THINK_LLM:-gpt-4o-mini}"
    echo "   Quick Think Model: ${QUICK_THINK_LLM:-gpt-4o-mini}"
    
    if [ "${OPENAI_BASE_URL}" != "https://api.openai.com/v1" ] && [ -n "${OPENAI_BASE_URL}" ]; then
        echo "🔗 检测到自建API服务器: ${OPENAI_BASE_URL}"
    fi
    
    if [ -n "${FEISHU_WEBHOOK_URL}" ]; then
        echo "📱 飞书机器人: 已配置"
    else
        echo "📱 飞书机器人: 未配置"
    fi
fi

# 创建必要的目录
mkdir -p results logs

# 构建和启动服务
echo "🔨 构建 Docker 镜像..."
docker-compose build

echo "🚀 启动服务..."
docker-compose up -d

echo "✅ 部署完成！"
echo ""
echo "📊 服务状态检查:"
docker-compose ps

echo ""
echo "📋 常用命令:"
echo "  查看日志: docker-compose logs -f tradingagents"
echo "  停止服务: docker-compose down"
echo "  重启服务: docker-compose restart"
echo "  测试分析: docker-compose exec tradingagents python trading_service.py test AAPL"
echo "  运行一次分析: docker-compose exec tradingagents python trading_service.py once"
echo ""
echo "📁 结果文件位置: ./results/"
echo "📋 日志文件位置: ./logs/"

# 等待服务启动
sleep 5

echo ""
echo "🔍 检查服务健康状态..."
if docker-compose exec tradingagents python -c "import sys; sys.path.append('/app'); from tradingagents.graph.trading_graph import TradingAgentsGraph; print('✅ TradingAgents 导入成功')"; then
    echo "✅ 服务启动成功！"
    
    # 显示API配置信息
    echo ""
    echo "🤖 LLM配置测试:"
    docker-compose exec tradingagents python -c "
import os
from tradingagents.default_config import DEFAULT_CONFIG
config = DEFAULT_CONFIG.copy()
print(f'Provider: {config[\"llm_provider\"]}')
print(f'API Endpoint: {config[\"backend_url\"]}')
print(f'Deep Model: {config[\"deep_think_llm\"]}')
print(f'Quick Model: {config[\"quick_think_llm\"]}')
"
else
    echo "❌ 服务启动可能有问题，请检查日志："
    echo "   docker-compose logs tradingagents"
    echo ""
    echo "🔧 常见问题排查:"
    echo "   1. 检查API密钥是否正确"
    echo "   2. 检查自建服务器地址是否可访问"
    echo "   3. 检查模型名称是否支持"
    echo "   4. 查看完整日志: docker-compose logs tradingagents"
fi

echo ""
echo "🎯 测试建议:"
echo "   # 测试单只股票分析"
echo "   docker-compose exec tradingagents python trading_service.py test AAPL"
echo ""
echo "   # 如果使用自建服务器，建议先测试简单模型"
echo "   # 可以在 .env 中设置："
echo "   # DEEP_THINK_LLM=gpt-3.5-turbo"
echo "   # QUICK_THINK_LLM=gpt-3.5-turbo"
