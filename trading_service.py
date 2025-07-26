import os
import sys
import json
import logging
import schedule
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any

# 添加项目路径
sys.path.append('/app')

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from integrations.feishu_bot import FeishuBot

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/trading_service.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingService:
    def __init__(self):
        # 初始化配置
        self.config = DEFAULT_CONFIG.copy()
        self.config["deep_think_llm"] = "gpt-4o-mini"  # 使用更便宜的模型
        self.config["quick_think_llm"] = "gpt-4o-mini"
        self.config["max_debate_rounds"] = 1
        self.config["online_tools"] = True
        
        # 初始化组件
        self.trading_graph = TradingAgentsGraph(debug=True, config=self.config)
        self.feishu_bot = FeishuBot()
        
        # 默认监控的股票列表
        self.default_tickers = [
            "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", 
            "NVDA", "META", "NFLX", "AMD", "INTC"
        ]
        
        # 从环境变量读取股票列表
        env_tickers = os.getenv('TRADING_TICKERS')
        if env_tickers:
            self.tickers = env_tickers.split(',')
        else:
            self.tickers = self.default_tickers
            
        logger.info(f"监控股票列表: {self.tickers}")
    
    def analyze_stock(self, ticker: str, date: str = None) -> Dict[str, Any]:
        """分析单只股票"""
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
            
        try:
            logger.info(f"开始分析股票: {ticker} (日期: {date})")
            
            # 运行交易分析
            state, decision = self.trading_graph.propagate(ticker, date)
            
            # 提取分析摘要
            analysis_summary = self._extract_analysis_summary(state)
            
            result = {
                'ticker': ticker,
                'date': date,
                'action': decision.get('action', 'HOLD'),
                'confidence': decision.get('confidence', 0.0),
                'reasoning': decision.get('reasoning', ''),
                'analysis_summary': analysis_summary,
                'timestamp': datetime.now().isoformat()
            }
            
            # 保存结果
            self._save_result(result)
            
            # 发送到飞书
            self.feishu_bot.send_trading_result(
                ticker, date, decision, analysis_summary
            )
            
            logger.info(f"股票 {ticker} 分析完成, 建议: {result['action']}")
            return result
            
        except Exception as e:
            error_msg = f"分析股票 {ticker} 时出错: {str(e)}"
            logger.error(error_msg)
            self.feishu_bot.send_error_notification(error_msg, ticker)
            return None
    
    def _extract_analysis_summary(self, state: Dict) -> str:
        """从状态中提取分析摘要"""
        summary_parts = []
        
        # 从各个分析师提取关键信息
        if 'fundamentals_analysis' in state:
            summary_parts.append(f"基本面: {state['fundamentals_analysis'][:100]}...")
        
        if 'technical_analysis' in state:
            summary_parts.append(f"技术面: {state['technical_analysis'][:100]}...")
            
        if 'news_analysis' in state:
            summary_parts.append(f"新闻面: {state['news_analysis'][:100]}...")
            
        if 'sentiment_analysis' in state:
            summary_parts.append(f"情绪面: {state['sentiment_analysis'][:100]}...")
        
        return "\n".join(summary_parts) if summary_parts else "无详细分析"
    
    def _save_result(self, result: Dict[str, Any]):
        """保存分析结果"""
        try:
            results_dir = '/app/results'
            os.makedirs(results_dir, exist_ok=True)
            
            filename = f"{result['ticker']}_{result['date']}.json"
            filepath = os.path.join(results_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            logger.error(f"保存结果失败: {str(e)}")
    
    def run_daily_analysis(self):
        """运行每日分析"""
        logger.info("开始每日股票分析...")
        results = []
        
        for ticker in self.tickers:
            try:
                result = self.analyze_stock(ticker)
                if result:
                    results.append(result)
                    
                # 避免API限制，添加延迟
                time.sleep(2)
                
            except Exception as e:
                logger.error(f"分析 {ticker} 时出错: {str(e)}")
                continue
        
        # 发送每日摘要
        if results:
            self.feishu_bot.send_daily_summary(results)
            logger.info(f"每日分析完成，共分析 {len(results)} 只股票")
        else:
            logger.warning("今日没有成功分析任何股票")
    
    def run_single_analysis(self, ticker: str):
        """运行单只股票分析（用于测试）"""
        return self.analyze_stock(ticker)

def main():
    """主函数"""
    # 创建日志目录
    os.makedirs('/app/logs', exist_ok=True)
    
    # 检查必要的环境变量
    required_env_vars = ['OPENAI_API_KEY', 'FINNHUB_API_KEY']
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        logger.error(f"缺少必要的环境变量: {missing_vars}")
        sys.exit(1)
    
    # 创建服务实例
    service = TradingService()
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            # 测试模式 - 分析单只股票
            ticker = sys.argv[2] if len(sys.argv) > 2 else "AAPL"
            logger.info(f"测试模式 - 分析股票: {ticker}")
            result = service.run_single_analysis(ticker)
            if result:
                print(json.dumps(result, indent=2, ensure_ascii=False))
            return
        elif sys.argv[1] == "once":
            # 运行一次完整分析
            logger.info("运行一次完整分析")
            service.run_daily_analysis()
            return
    
    # 定时任务模式
    logger.info("启动定时分析服务...")
    
    # 设置定时任务 - 每个交易日早上9点运行
    schedule.every().monday.at("09:00").do(service.run_daily_analysis)
    schedule.every().tuesday.at("09:00").do(service.run_daily_analysis)
    schedule.every().wednesday.at("09:00").do(service.run_daily_analysis)
    schedule.every().thursday.at("09:00").do(service.run_daily_analysis)
    schedule.every().friday.at("09:00").do(service.run_daily_analysis)
    
    # 可选：市场收盘后的分析
    schedule.every().monday.at("16:30").do(service.run_daily_analysis)
    schedule.every().tuesday.at("16:30").do(service.run_daily_analysis)
    schedule.every().wednesday.at("16:30").do(service.run_daily_analysis)
    schedule.every().thursday.at("16:30").do(service.run_daily_analysis)
    schedule.every().friday.at("16:30").do(service.run_daily_analysis)
    
    logger.info("定时任务已设置，等待执行...")
    
    # 运行调度器
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次

if __name__ == "__main__":
    main()
