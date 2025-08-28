#!/bin/bash

# TradingAgents 启动脚本
# 自动激活虚拟环境并运行项目

set -e  # 遇到错误时退出

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${PROJECT_DIR}/venv"

echo "🚀 TradingAgents 启动脚本"
echo "=" * 50

# 检查虚拟环境
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ 未找到虚拟环境，正在创建..."
    python3 -m venv venv
    echo "✅ 虚拟环境创建完成"
fi

# 激活虚拟环境
source "$VENV_DIR/bin/activate"
echo "✅ 虚拟环境已激活: $(which python)"

# 检查依赖
echo "🔍 检查依赖包..."
if ! python -c "import langchain_openai" 2>/dev/null; then
    echo "📦 正在安装依赖包..."
    pip install -r requirements.txt
    echo "✅ 依赖包安装完成"
else
    echo "✅ 依赖包已安装"
fi

# 检查API密钥
echo "🔑 检查API密钥..."
if [ -z "$OPENAI_API_KEY" ] || [ -z "$FINNHUB_API_KEY" ]; then
    echo "⚠️  缺少API密钥环境变量"
    echo "请设置以下环境变量:"
    echo "  export OPENAI_API_KEY=your_openai_api_key"
    echo "  export FINNHUB_API_KEY=your_finnhub_api_key"
    echo ""
    echo "或者创建 .env 文件（参考 .env.example）"
    echo ""
fi

# 运行环境检查
echo "🔧 运行环境检查..."
python check_env.py

echo ""
echo "🎯 可用的运行命令："
echo "  python main.py                    # 运行主脚本"
echo "  python -m cli.main               # 运行交互式CLI"
echo "  python -m cli.main analyze       # 直接运行分析"
echo ""

# 如果提供了参数，则运行相应的命令
if [ $# -gt 0 ]; then
    echo "🚀 正在运行: $@"
    exec "$@"
else
    echo "💡 提示：您可以在激活的虚拟环境中运行上述任意命令"
    echo "或者使用: ./start.sh python main.py"
fi