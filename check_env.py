#!/usr/bin/env python3
"""
环境测试脚本 - 验证TradingAgents运行环境
"""
import os
import sys
from pathlib import Path

def check_python_version():
    """检查Python版本"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        print(f"✅ Python版本: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python版本过低: {version.major}.{version.minor}.{version.micro} (需要>=3.10)")
        return False

def check_dependencies():
    """检查依赖包"""
    required_packages = [
        "langchain_openai",
        "langchain_anthropic", 
        "langchain_google_genai",
        "langgraph",
        "pandas",
        "yfinance",
        "rich",
        "typer"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} (未安装)")
            missing_packages.append(package)
    
    return len(missing_packages) == 0

def check_api_keys():
    """检查API密钥"""
    api_keys = {
        "FINNHUB_API_KEY": "FinnHub (必需)",
        "OPENAI_API_KEY": "OpenAI (必需)",
        "ANTHROPIC_API_KEY": "Anthropic (可选)",
        "GOOGLE_API_KEY": "Google (可选)"
    }
    
    all_required_set = True
    for key, description in api_keys.items():
        value = os.getenv(key)
        if value:
            print(f"✅ {key}: 已设置 ({description})")
        else:
            if "必需" in description:
                print(f"❌ {key}: 未设置 ({description})")
                all_required_set = False
            else:
                print(f"⚠️  {key}: 未设置 ({description})")
    
    return all_required_set

def check_project_structure():
    """检查项目结构"""
    required_dirs = [
        "tradingagents",
        "tradingagents/graph",
        "tradingagents/agents", 
        "cli"
    ]
    
    required_files = [
        "main.py",
        "requirements.txt",
        "tradingagents/default_config.py",
        "cli/main.py"
    ]
    
    all_present = True
    
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"✅ 目录: {dir_path}")
        else:
            print(f"❌ 目录: {dir_path} (不存在)")
            all_present = False
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ 文件: {file_path}")
        else:
            print(f"❌ 文件: {file_path} (不存在)")
            all_present = False
    
    return all_present

def main():
    """主函数"""
    print("🔍 TradingAgents 环境检查")
    print("=" * 50)
    
    checks = [
        ("Python版本", check_python_version),
        ("项目结构", check_project_structure),
        ("依赖包", check_dependencies),
        ("API密钥", check_api_keys)
    ]
    
    all_passed = True
    for name, check_func in checks:
        print(f"\n📋 检查 {name}:")
        passed = check_func()
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 环境检查通过！可以运行TradingAgents")
    else:
        print("⚠️  存在问题，请根据上述提示修复")
        print("\n💡 解决建议:")
        print("1. 确保在虚拟环境中运行: source venv/bin/activate")
        print("2. 安装依赖: pip install -r requirements.txt") 
        print("3. 设置API密钥: export OPENAI_API_KEY=your_key")
        print("4. 参考 CLAUDE.md 获取详细指导")

if __name__ == "__main__":
    main()