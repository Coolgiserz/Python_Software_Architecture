"""
单例模式

单例：一个类，该类仅有一个实例和一个明确定义的访问点

要求：
1. 一个类必须有且只有一个实例，该实例通过一个众所周知的访问点访问
2. 通过继承扩展后不会破坏模式


场景（什么情况下我们希望类只有一个实例）：
    使用场景：
    1. 频繁实例化和销毁的对象
    2. 经常使用但实例化耗费较多时间和资源
    3. 需要资源共享

    应用场景：
    1. 计数器：同步技术
    2. 数据库连接池：节省打开或者关闭数据库链接引起的效率损耗
    3. 线程池
    4. 文件系统

"""

class Singleton(object):
    # 用于保存类的单个实例
    _instance = None
    def __new__(cls, *args, **kwargs):
        """
        构造方法，在此创造类实例
        :param args:
        :param kwargs:
        """
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

def test_singleton(cls):
    return cls() == cls()

class SingletonA(Singleton):
    pass
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    s3 = SingletonA()
    assert s1 == s2
    assert s1 == s3

    print(s1,s2,s3)
    print(test_singleton(SingletonA))