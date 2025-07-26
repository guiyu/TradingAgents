import json
import requests
import os
from datetime import datetime
from typing import Dict, Any
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FeishuBot:
    def __init__(self, webhook_url: str = None):
        self.webhook_url = webhook_url or os.getenv('FEISHU_WEBHOOK_URL')
        if not self.webhook_url:
            logger.warning("飞书Webhook URL未配置，将跳过消息发送")
    
    def send_trading_result(self, ticker: str, date: str, decision: Dict[str, Any], 
                          analysis_summary: str = None):
        """发送交易结果到飞书群"""
        if not self.webhook_url:
            logger.info("跳过飞书消息发送 - 未配置webhook")
            return
        
        # 格式化决策信息
        action = decision.get('action', 'HOLD')
        confidence = decision.get('confidence', 0)
        reasoning = decision.get('reasoning', '无具体分析')
        
        # 构建富文本消息
        card_content = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "content": f"🤖 **TradingAgents 交易建议**",
                            "tag": "lark_md"
                        }
                    },
                    {
                        "tag": "hr"
                    },
                    {
                        "tag": "div",
                        "fields": [
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**股票代码**: {ticker}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**分析日期**: {date}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**建议操作**: {self._format_action(action)}",
                                    "tag": "lark_md"
                                }
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**置信度**: {confidence:.2%}",
                                    "tag": "lark_md"
                                }
                            }
                        ]
                    },
                    {
                        "tag": "div",
                        "text": {
                            "content": f"**分析摘要**:\n{reasoning[:500]}{'...' if len(reasoning) > 500 else ''}",
                            "tag": "lark_md"
                        }
                    }
                ]
            }
        }
        
        # 如果有详细分析，添加到消息中
        if analysis_summary:
            card_content["card"]["elements"].append({
                "tag": "hr"
            })
            card_content["card"]["elements"].append({
                "tag": "div",
                "text": {
                    "content": f"**详细分析**:\n{analysis_summary[:800]}{'...' if len(analysis_summary) > 800 else ''}",
                    "tag": "lark_md"
                }
            })
        
        # 添加时间戳
        card_content["card"]["elements"].append({
            "tag": "div",
            "text": {
                "content": f"⏰ 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "tag": "lark_md"
            }
        })
        
        try:
            response = requests.post(
                self.webhook_url,
                json=card_content,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 200:
                logger.info(f"飞书消息发送成功: {ticker} - {action}")
            else:
                logger.error(f"飞书消息发送失败: {response.status_code} - {response.text}")
                
        except Exception as e:
            logger.error(f"发送飞书消息时出错: {str(e)}")
    
    def _format_action(self, action: str) -> str:
        """格式化交易操作"""
        action_map = {
            'BUY': '🟢 买入',
            'SELL': '🔴 卖出',
            'HOLD': '🟡 持有',
            'STRONG_BUY': '🟢🟢 强烈买入',
            'STRONG_SELL': '🔴🔴 强烈卖出'
        }
        return action_map.get(action.upper(), f"⚪ {action}")
    
    def send_error_notification(self, error_msg: str, ticker: str = None):
        """发送错误通知"""
        if not self.webhook_url:
            return
            
        message = {
            "msg_type": "text",
            "content": {
                "text": f"⚠️ TradingAgents 错误通知\n"
                       f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                       f"股票: {ticker or '未知'}\n"
                       f"错误: {error_msg}"
            }
        }
        
        try:
            requests.post(self.webhook_url, json=message, timeout=10)
        except Exception as e:
            logger.error(f"发送错误通知失败: {str(e)}")

    def send_daily_summary(self, results: list):
        """发送每日交易摘要"""
        if not self.webhook_url or not results:
            return
            
        summary_text = f"📊 **每日交易摘要** - {datetime.now().strftime('%Y-%m-%d')}\n\n"
        
        for result in results:
            ticker = result.get('ticker', 'N/A')
            action = result.get('action', 'HOLD')
            confidence = result.get('confidence', 0)
            summary_text += f"• {ticker}: {self._format_action(action)} (置信度: {confidence:.1%})\n"
        
        message = {
            "msg_type": "text",
            "content": {"text": summary_text}
        }
        
        try:
            requests.post(self.webhook_url, json=message, timeout=10)
            logger.info("每日摘要发送成功")
        except Exception as e:
            logger.error(f"发送每日摘要失败: {str(e)}")
