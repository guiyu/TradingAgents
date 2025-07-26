#!/usr/bin/env python3
"""
TradingAgents API配置测试脚本
用于验证自建API服务器的配置是否正确
"""

import os
import sys
import json
from datetime import datetime

# 添加项目路径
sys.path.append('.')

def test_environment_variables():
    """测试环境变量配置"""
    print("🔧 环境变量配置检查:")
    
    required_vars = ['OPENAI_API_KEY', 'FINNHUB_API_KEY']
    optional_vars = ['OPENAI_BASE_URL', 'API_KEY', 'LLM_PROVIDER', 'DEEP_THINK_LLM', 'QUICK_THINK_LLM']
    
    # 检查必需的环境变量
    missing_required = []
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # 不显示完整的API密钥，只显示前几位和后几位
            if 'KEY' in var and len(value) > 10:
                masked_value = f"{value[:6]}...{value[-4:]}"
            else:
                masked_value = value
            print(f"  ✅ {var}: {masked_value}")
        else:
            print(f"  ❌ {var}: 未设置")
            missing_required.append(var)
    
    # 检查可选的环境变量
    for var in optional_vars:
        value = os.getenv(var)
        if value:
            print(f"  ℹ️  {var}: {value}")
        else:
            print(f"  ⚪ {var}: 使用默认值")
    
    if missing_required:
        print(f"\n❌ 缺少必需的环境变量: {missing_required}")
        return False
    
    print("\n✅ 环境变量配置检查通过")
    return True

def test_config_loading():
    """测试配置加载"""
    print("\n📋 TradingAgents配置加载测试:")
    
    try:
        from tradingagents.default_config import DEFAULT_CONFIG
        config = DEFAULT_CONFIG.copy()
        
        print(f"  🤖 LLM Provider: {config['llm_provider']}")
        print(f"  🔗 API Endpoint: {config['backend_url']}")
        print(f"  🧠 Deep Think Model: {config['deep_think_llm']}")
        print(f"  ⚡ Quick Think Model: {config['quick_think_llm']}")
        print(f"  🛠️  Online Tools: {config['online_tools']}")
        
        # 检查自建服务器配置
        if config["backend_url"] != "https://api.openai.com/v1":
            print(f"  🔗 检测到自建API服务器: {config['backend_url']}")
        
        print("\n✅ 配置加载成功")
        return True, config
        
    except Exception as e:
        print(f"\n❌ 配置加载失败: {str(e)}")
        return False, None

def test_llm_initialization():
    """测试LLM初始化"""
    print("\n🤖 LLM初始化测试:")
    
    try:
        from tradingagents.graph.trading_graph import TradingAgentsGraph
        
        # 创建最小配置进行测试
        print("  正在初始化TradingAgents...")
        ta = TradingAgentsGraph(debug=True, selected_analysts=["market"])
        
        print("  ✅ TradingAgents初始化成功")
        print(f"  🧠 Deep LLM: {ta.deep_thinking_llm.__class__.__name__}")
        print(f"  ⚡ Quick LLM: {ta.quick_thinking_llm.__class__.__name__}")
        
        return True, ta
        
    except Exception as e:
        print(f"  ❌ LLM初始化失败: {str(e)}")
        print(f"  💡 建议检查API密钥和服务器地址是否正确")
        return False, None

def test_simple_api_call():
    """测试简单的API调用"""
    print("\n🔍 API连接测试:")
    
    try:
        from langchain_openai import ChatOpenAI
        from tradingagents.default_config import DEFAULT_CONFIG
        
        config = DEFAULT_CONFIG.copy()
        
        # 构建LLM参数
        llm_kwargs = {}
        if config.get("backend_url"):
            llm_kwargs["base_url"] = config["backend_url"]
        if config.get("api_key") or config.get("openai_api_key"):
            llm_kwargs["api_key"] = config.get("api_key") or config.get("openai_api_key")
        
        # 创建测试LLM
        test_llm = ChatOpenAI(
            model=config["quick_think_llm"],
            **llm_kwargs
        )
        
        print("  正在发送测试请求...")
        
        # 发送简单的测试消息
        response = test_llm.invoke("Hello! Please respond with 'API connection successful'")
        
        print(f"  ✅ API调用成功")
        print(f"  📝 响应内容: {response.content[:100]}{'...' if len(response.content) > 100 else ''}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ API调用失败: {str(e)}")
        print(f"  💡 请检查:")
        print(f"     - API密钥是否正确")
        print(f"     - 服务器地址是否可访问")
        print(f"     - 模型名称是否支持")
        return False

def main():
    """主测试函数"""
    print("🚀 TradingAgents API配置测试")
    print("=" * 50)
    
    # 测试步骤
    tests = [
        ("环境变量检查", test_environment_variables),
        ("配置加载测试", lambda: test_config_loading()[0]),
        ("LLM初始化测试", lambda: test_llm_initialization()[0]),
        ("API连接测试", test_simple_api_call),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name}执行失败: {str(e)}")
            results.append((test_name, False))
    
    # 汇总结果
    print("\n" + "=" * 50)
    print("📊 测试结果汇总:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有测试通过！TradingAgents配置正确")
        print("\n🎯 接下来可以:")
        print("  1. 运行完整分析: python trading_service.py test AAPL")
        print("  2. 启动定时服务: python trading_service.py")
        print("  3. 运行一次分析: python trading_service.py once")
    else:
        print("⚠️ 部分测试失败，请检查配置")
        print("\n🔧 故障排除建议:")
        print("  1. 检查 .env 文件中的配置")
        print("  2. 验证API密钥是否有效")
        print("  3. 确认服务器地址是否可访问")
        print("  4. 查看详细错误信息并相应调整")
    
    return all_passed

if __name__ == "__main__":
    # 支持命令行参数
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("TradingAgents API配置测试脚本")
        print("\n用法:")
        print("  python test_api_config.py          # 运行所有测试")
        print("  python test_api_config.py --help   # 显示帮助")
        print("\n环境变量:")
        print("  OPENAI_API_KEY     - OpenAI API密钥 (必需)")
        print("  OPENAI_BASE_URL    - API服务器地址 (可选)")
        print("  FINNHUB_API_KEY    - FinnHub API密钥 (必需)")
        print("  LLM_PROVIDER       - LLM提供商 (可选)")
        print("  DEEP_THINK_LLM     - 深度思考模型 (可选)")
        print("  QUICK_THINK_LLM    - 快速思考模型 (可选)")
        sys.exit(0)
    
    success = main()
    sys.exit(0 if success else 1)
