"""
单例模式
singlelon中的Singleton类存在问题：子类的实例与父类的实例时同一个实例，原因是子类创建时也返回了在父类中定义的_instance，所以子类、父类的实例位于相同的内存地址
本文件实现通过__name__属性，区分子类与父类的实例对象
"""

class Singleton(object):
    # 用于保存类的单个实例
    def __new__(cls, *args, **kwargs):
        """
        构造方法，在此创造类实例
        :param args:
        :param kwargs:
        """
        instance_name = f"{cls.__name__}_instance"
        _instance = getattr(cls, instance_name, None)
        if not _instance:
            _instance = object.__new__(cls)
            setattr(cls, instance_name, _instance)
        return _instance

def test_singleton(cls):
    return cls() == cls()

class SingletonA(Singleton):
    pass
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    s3 = SingletonA()
    s4 = SingletonA()

    # assert s1 == s2
    # assert s1 == s3

    print(s1,s2,s3, s4)
    print(test_singleton(SingletonA))