from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"  # Use OpenAI provider
config["backend_url"] = "https://poloai.top/token/v1"  # Use provided backend URL
config["deep_think_llm"] = "gpt-4o"  # Use GPT-4o for deep thinking
config["quick_think_llm"] = "gpt-4o-mini"  # Use GPT-4o-mini for quick thinking
config["max_debate_rounds"] = 1  # Debate rounds
config["online_tools"] = True  # Enable online tools

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
