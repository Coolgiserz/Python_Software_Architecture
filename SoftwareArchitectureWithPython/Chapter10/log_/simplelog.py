"""
日志记录
"""
import logging
if __name__ == "__main__":


    # 配置日志记录 注意：basicConfig需要在日志打印前配置
    logging.basicConfig(filename="./simple.log_", level=logging.DEBUG, format="%(asctime)s %(message)s")
    logging.warning("This is a simple log.")
    logging.info("Come on")
    logging.info("Come on!")
