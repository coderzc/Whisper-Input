#!/bin/bash

# 查找并终止进程
if pgrep -f "python main.py" > /dev/null; then
    pkill -f "python main.py"
    echo "Whisper Input 已停止运行"
else
    echo "Whisper Input 未在运行"
fi 