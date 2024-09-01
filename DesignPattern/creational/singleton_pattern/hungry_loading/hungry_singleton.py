"""
饿汉单例模式
"""
class SingletonModule:
    class _SingletonModule:
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            self.config = None

    _instance = _SingletonModule()

    def __new__(cls, *args, **kwargs):
        return cls._instance

a = SingletonModule()
b = SingletonModule()
print(a is b)


