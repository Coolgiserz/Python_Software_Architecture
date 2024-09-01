"""
将单例放到一个单独的模块
"""
class _SingletonModule:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.config = None

config = _SingletonModule()