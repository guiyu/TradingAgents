FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir requests schedule

# 复制项目代码
COPY . .

# 创建必要的目录
RUN mkdir -p /app/results /app/logs

# 设置环境变量
ENV PYTHONPATH=/app
ENV TRADINGAGENTS_RESULTS_DIR=/app/results

# 暴露端口（如果需要Web界面）
EXPOSE 8000

# 默认启动定时服务
CMD ["python", "trading_service.py"]
