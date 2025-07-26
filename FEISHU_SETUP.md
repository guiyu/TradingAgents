# 飞书机器人配置指南

## 1. 创建飞书自定义机器人

### 步骤 1: 在飞书群中添加机器人
1. 打开飞书群聊
2. 点击右上角的 "..." 菜单
3. 选择 "设置" -> "群机器人"
4. 点击 "添加机器人" -> "自定义机器人"

### 步骤 2: 配置机器人
1. 设置机器人名称: "TradingAgents"
2. 设置机器人描述: "AI交易分析助手"
3. 选择机器人头像（可选）
4. 点击 "下一步"

### 步骤 3: 获取 Webhook URL
1. 复制生成的 Webhook URL
2. URL 格式类似: `https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxx`
3. 将此 URL 添加到 `.env` 文件中

## 2. 配置环境变量

编辑 `.env` 文件，添加飞书机器人配置：

```bash
# 飞书机器人 Webhook URL
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/你的webhook_token
```

## 3. 测试机器人

部署服务后，可以通过以下命令测试机器人：

```bash
# 测试单只股票分析（会发送到飞书群）
docker-compose exec tradingagents python trading_service.py test AAPL
```

## 4. 消息格式说明

机器人会发送以下类型的消息：

### 交易建议消息
- 包含股票代码、分析日期、建议操作、置信度
- 提供分析摘要和详细分析
- 使用富文本卡片格式，美观易读

### 错误通知消息
- 当分析过程出现错误时发送
- 包含错误详情和时间戳

### 每日摘要消息
- 每日分析完成后发送汇总信息
- 列出所有分析的股票和建议

## 5. 安全建议

1. **保护 Webhook URL**: 不要将 Webhook URL 泄露给他人
2. **访问控制**: 只在信任的群聊中使用机器人
3. **定期更新**: 如有安全问题，可重新生成 Webhook URL

## 6. 自定义配置

可以通过环境变量自定义机器人行为：

```bash
# 自定义监控的股票列表（逗号分隔）
TRADING_TICKERS=AAPL,MSFT,GOOGL,TSLA,NVDA

# 其他配置...
```

## 7. 故障排除

### 消息发送失败
- 检查 Webhook URL 是否正确
- 确认机器人未被群管理员禁用
- 查看容器日志: `docker-compose logs tradingagents`

### 消息格式问题
- 飞书对消息长度有限制，过长的内容会被截断
- 确保 JSON 格式正确

---

配置完成后，TradingAgents 会自动将分析结果发送到您的飞书群聊中！
