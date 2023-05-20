"""
高级日志记录：自定义格式和日志记录器

场景：分析程序性能，记录每个函数或方法需要时间（通过定制的日志记录器完成）

扩展：
更多python日志记录处理程序（Handler），参见：https://docs.python.org/3/library/logging.handlers.html
"""
import logging
import time
from functools import partial

class LoggerWrapper(object):
    def __init__(self, app_name, filename=None, level=logging.INFO, console=False):
        self.log = logging.getLogger(app_name)
        self.log.setLevel(level)

        # 添加处理程序
        if console:
            self.log.addHandler(logging.StreamHandler())
        if filename:
            self.log.addHandler(logging.FileHandler(filename=filename))

        # 设置日志格式化
        for handle in self.log.handlers:
            formatter = logging.Formatter("%(asctime)s [%(timespent)s]: %(levelname)-8s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
            handle.setFormatter(fmt=formatter)

        for name in ("debug", "info", "warning", "error", "critical"):
            func = partial(self._dolog, name)
            # 把这些名称设置为LoggerWrapper类的成员方法
            setattr(self, name, func)

        self._markt = time.time()

    def _calc_time(self):
        """计算两次日志记录之间的耗时"""
        tnow = time.time()
        tdiff = int(round(tnow - self._markt))
        hr, rem = divmod(tdiff, 3600)
        mins, sec = divmod(rem, 60)
        self._markt = tnow
        return "%.2d:%.2d:%.2d" % (hr, mins, sec)

    def _dolog(self, levelname, msg, *args, **kwargs):
        logfunc = getattr(self.log, levelname)
        return logfunc(msg, *args, extra={"timespent": self._calc_time()})

if __name__ == "__main__":
    log = LoggerWrapper("testlog", filename="log.log", console=True)
    log.info("Start recording...")
    log.info("recording...")
    sum = 0
    for i in range(100000000):
        sum += i
    log.info("finished")


