import logging
import colorlog

# 添加自定义日志级别
RECOGNITION = 25  # 在 INFO(20) 和 WARNING(30) 之间
logging.addLevelName(RECOGNITION, 'RECOGNITION')

def recognition(self, message, *args, **kwargs):
    if self.isEnabledFor(RECOGNITION):
        self._log(RECOGNITION, message, args, **kwargs)

logging.Logger.recognition = recognition

def setup_logger():
    """配置彩色日志"""
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        fmt='%(asctime)s - %(log_color)s%(levelname)-8s%(reset)s - %(message)s',
        datefmt='%H:%M:%S',
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'RECOGNITION': 'red,bold',  # 添加识别结果的颜色配置
            'WARNING': 'yellow',
            'ERROR':   'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    ))
    
    logger = colorlog.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    # 移除可能存在的默认处理器
    for handler in logger.handlers[:-1]:
        logger.removeHandler(handler)
    
    return logger

logger = setup_logger() 