#!/bin/bash

# TradingAgents 部署脚本

set -e

echo "🚀 开始部署 TradingAgents 服务..."

# 检查环境变量配置文件
if [ ! -f ".env" ]; then
    echo "⚠️  未找到 .env 文件，请先配置 API 密钥"
    echo "📝 复制 .env.example 到 .env 并填入您的 API 密钥:"
    echo "   cp .env.example .env"
    echo "   然后编辑 .env 文件填入真实的 API 密钥"
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
else
    echo "❌ 服务启动可能有问题，请检查日志："
    echo "   docker-compose logs tradingagents"
fi
