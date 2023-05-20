"""
使用日志记录器对象
1. 自定义日志格式
2. 写入系统日志
"""
import logging
def create_logger(app_name, logfilename=None, level=logging.INFO, console=False):
    """
    1. 创建logger对象
    2. 配置处理程序（控制台、文件、套接字）
    3. 设置日志级别
    4. 格式化日志消息
    :param app_name:
    :param logfilename:
    :param level:
    :param console:
    :return:
    """
    log = logging.getLogger(name=app_name)
    log.setLevel(level)
    if logfilename is not None:
        log.addHandler(logging.FileHandler(logfilename))
    if console:
        log.addHandler(logging.StreamHandler())
    # 格式化
    formatter = logging.Formatter(f"{log.name} %(asctime)s : %(levelname)- 8s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    # formatter = logging.Formatter("%(asctime)s:%(levelname)-8s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    for handle in log.handlers:

        handle.setFormatter(formatter)
    return log

if __name__ == "__main__":
    log = create_logger("app", logfilename="app.log", console=True)
    log.info("Start recording")
    log.info("Start initialzing")

    log1 = create_logger("app1", logfilename="app.log", console=True)
    log1.info("Start recording")
    log1.info("Start initialzing")
