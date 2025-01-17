#!/bin/bash

# 检查进程是否已在运行
if pgrep -f "python main.py" > /dev/null; then
    echo "Whisper Input 已经在运行中"
    exit 1
fi

# 创建日志目录
mkdir -p logs

# 激活虚拟环境（如果存在）并启动程序
if [ -d "venv" ]; then
    source venv/bin/activate
    nohup python main.py > logs/whisper_input.log 2>&1 &
else
    nohup python main.py > logs/whisper_input.log 2>&1 &
fi

echo "Whisper Input 已在后台启动"
echo "日志文件位置: logs/whisper_input.log"