import logging
import os
import time

# 获取项目的根目录
root_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
log_path = os.path.join(root_path, 'log')

# 打印日志路径
print(log_path)

# 如果日志目录不存在，则创建
if not os.path.exists(log_path):
    os.mkdir(log_path)

class Logger:
    def __init__(self):
        # 获取当前日期
        current_date = time.strftime("%Y-%m-%d")
        # 创建日期文件夹
        date_folder = os.path.join(log_path, current_date)
        if not os.path.exists(date_folder):
            os.mkdir(date_folder)

        # 定义日志文件名
        log_filename = "{}.log".format(time.strftime("%H点%M分%S秒"))
        self.logname = os.path.join(date_folder, log_filename)

        # 定义一个日志容器
        self.logger = logging.getLogger("log")
        # 设置日志打印的级别
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入的格式
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        # 创建日志处理器，用来存放日志文件
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置控制台打印日志级别
        self.console.setLevel(logging.DEBUG)
        # 文件存放日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # 文件存放日志格式
        self.filelogger.setFormatter(self.formater)
        # 控制台打印日志格式
        self.console.setFormatter(self.formater)
        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

logger = Logger().logger

if __name__ == '__main__':
    logger.info("---INFO日志---")
    logger.debug("---DEBUG日志---")
    logger.warning("---WARNING日志---")
    logger.error("---ERROR日志---")
    logger.critical("---CRITICAL日志---")
