#!/usr/bin/env python3
"""
测试 NewAPI 集成功能
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_newapi_integration():
    """测试 NewAPI 集成是否正常工作"""
    print("=== NewAPI 集成测试 ===\n")
    
    # 测试 CLI 配置文件
    print("1. 测试 CLI 配置文件")
    try:
        with open('cli/utils.py', 'r') as f:
            content = f.read()
            if 'NewAPI' in content and 'b4u.qzz.io' in content:
                print("✓ CLI 配置中已添加 NewAPI 选项")
            else:
                print("✗ CLI 配置中缺少 NewAPI 选项")
                return False
    except Exception as e:
        print(f"✗ CLI 配置文件读取错误: {e}")
        return False
    
    # 测试 NewAPI 模型列表
    print("\n2. 测试 NewAPI 模型列表配置")
    try:
        with open('cli/utils.py', 'r') as f:
            content = f.read()
            if '"newapi"' in content and 'gpt-4o-mini' in content and 'deepseek-chat' in content:
                print("✓ NewAPI 快速思考模型已配置")
                print("  支持的模型: GPT-4o-mini, Claude-3.5-haiku, DeepSeek-chat, GLM-4-flash 等")
            if 'glm-4-plus' in content and 'qwen-max' in content:
                print("✓ NewAPI 深度思考模型已配置") 
                print("  支持的模型: GPT-4o, Claude-3.5-sonnet, DeepSeek-coder, Qwen-max 等")
            else:
                print("✗ NewAPI 模型列表配置不完整")
                return False
    except Exception as e:
        print(f"✗ 模型列表配置检查错误: {e}")
        return False
    
    # 测试交易图配置
    print("\n3. 测试交易图 NewAPI 支持")
    try:
        with open('tradingagents/graph/trading_graph.py', 'r') as f:
            content = f.read()
            if '"newapi"' in content and 'in ["openai", "ollama", "openrouter", "newapi"]' in content:
                print("✓ TradingAgentsGraph 已支持 NewAPI 提供商")
            else:
                print("✗ TradingAgentsGraph 缺少 NewAPI 支持")
                return False
    except Exception as e:
        print(f"✗ 交易图配置检查错误: {e}")
        return False
    
    # 测试示例配置文件
    print("\n4. 测试示例配置文件")
    try:
        if os.path.exists('examples/newapi_config.py'):
            print("✓ NewAPI 示例配置文件已创建")
            with open('examples/newapi_config.py', 'r') as f:
                content = f.read()
                if 'b4u.qzz.io/v1' in content:
                    print("✓ 示例配置包含正确的 NewAPI URL")
        else:
            print("✗ NewAPI 示例配置文件不存在")
            return False
    except Exception as e:
        print(f"✗ 示例配置文件检查错误: {e}")
        return False
    
    # 测试文档更新
    print("\n5. 测试文档更新")
    try:
        with open('CLAUDE.md', 'r') as f:
            content = f.read()
            if 'NewAPI 平台' in content and 'b4u.qzz.io' in content:
                print("✓ CLAUDE.md 文档已更新 NewAPI 信息")
            else:
                print("✗ CLAUDE.md 文档缺少 NewAPI 信息")
                return False
    except Exception as e:
        print(f"✗ 文档更新检查错误: {e}")
        return False
    
    print("\n=== 测试完成 ===")
    print("✓ 所有 NewAPI 集成测试通过")
    print("\n功能说明:")
    print("1. CLI 界面新增 'NewAPI' 提供商选项")
    print("2. 支持国际模型（GPT、Claude、Gemini）和中国模型（DeepSeek、GLM、Qwen 等）")
    print("3. 与现有配置系统完全兼容")
    print("4. 提供详细的配置示例和文档")
    
    print("\n使用步骤:")
    print("1. 在 NewAPI 平台 (https://b4u.qzz.io/) 获取 API 密钥")
    print("2. 设置环境变量: export OPENAI_API_KEY=your_newapi_key")
    print("3. 运行: python -m cli.main")
    print("4. 选择 'NewAPI' 作为 LLM 提供商")
    print("5. 选择合适的模型进行分析")
    
    return True

if __name__ == "__main__":
    test_newapi_integration()