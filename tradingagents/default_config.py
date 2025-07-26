import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings - 支持自建API服务器
    "llm_provider": os.getenv("LLM_PROVIDER", "openai"),
    "deep_think_llm": os.getenv("DEEP_THINK_LLM", "gpt-4o-mini"),
    "quick_think_llm": os.getenv("QUICK_THINK_LLM", "gpt-4o-mini"),
    # 支持自定义API端点
    "backend_url": os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    # 兼容性设置 - 支持其他API提供商
    "api_key": os.getenv("API_KEY", os.getenv("OPENAI_API_KEY")),
    # Debate and discussion settings
    "max_debate_rounds": int(os.getenv("MAX_DEBATE_ROUNDS", "1")),
    "max_risk_discuss_rounds": int(os.getenv("MAX_RISK_DISCUSS_ROUNDS", "1")),
    "max_recur_limit": int(os.getenv("MAX_RECUR_LIMIT", "100")),
    # Tool settings
    "online_tools": os.getenv("ONLINE_TOOLS", "True").lower() == "true",
}
