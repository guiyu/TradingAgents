"""
示例：使用 NewAPI 平台配置 TradingAgents

NewAPI 是一个统一的 API 管理平台，支持多个 AI 模型提供商，
包括 OpenAI、Anthropic Claude、Google Gemini、DeepSeek、ChatGLM 等。

使用方法：
1. 在 NewAPI 平台 (https://b4u.qzz.io/) 获取 API 密钥
2. 设置环境变量：export OPENAI_API_KEY=your_newapi_key
3. 运行此配置
"""

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# NewAPI 配置示例
config = DEFAULT_CONFIG.copy()
config.update({
    "llm_provider": "newapi",
    "backend_url": "https://b4u.qzz.io/v1",
    "deep_think_llm": "gpt-4o",  # 使用 GPT-4o 进行深度思考
    "quick_think_llm": "gpt-4o-mini",  # 使用 GPT-4o-mini 进行快速思考
    "max_debate_rounds": 2,
    "online_tools": True,
})

# 中国模型配置示例
config_chinese = DEFAULT_CONFIG.copy()
config_chinese.update({
    "llm_provider": "newapi",
    "backend_url": "https://b4u.qzz.io/v1", 
    "deep_think_llm": "deepseek-coder",  # 使用 DeepSeek 进行深度思考
    "quick_think_llm": "glm-4-flash",    # 使用 GLM-4 进行快速思考
    "max_debate_rounds": 1,
    "online_tools": True,
})

# Claude 模型配置示例
config_claude = DEFAULT_CONFIG.copy()
config_claude.update({
    "llm_provider": "newapi", 
    "backend_url": "https://b4u.qzz.io/v1",
    "deep_think_llm": "claude-3-5-sonnet-20241022",  # 使用 Claude Sonnet 进行深度思考
    "quick_think_llm": "claude-3-5-haiku-20241022",  # 使用 Claude Haiku 进行快速思考
    "max_debate_rounds": 3,
    "online_tools": True,
})

if __name__ == "__main__":
    print("NewAPI 平台配置示例")
    print("1. 国际模型配置 (GPT-4o)")
    print("2. 中国模型配置 (DeepSeek + GLM)")
    print("3. Claude 模型配置")
    
    choice = input("请选择配置 (1/2/3): ")
    
    if choice == "1":
        selected_config = config
        print("使用国际模型配置...")
    elif choice == "2":
        selected_config = config_chinese
        print("使用中国模型配置...")
    elif choice == "3":
        selected_config = config_claude
        print("使用 Claude 模型配置...")
    else:
        print("无效选择，使用默认配置")
        selected_config = config
    
    # 初始化交易智能体
    ta = TradingAgentsGraph(debug=True, config=selected_config)
    
    # 运行分析
    ticker = input("请输入股票代码 (默认: NVDA): ") or "NVDA"
    date = input("请输入分析日期 (默认: 2024-05-10): ") or "2024-05-10"
    
    print(f"开始分析 {ticker} 在 {date} 的交易决策...")
    _, decision = ta.propagate(ticker, date)
    print(f"分析完成！决策结果：{decision}")