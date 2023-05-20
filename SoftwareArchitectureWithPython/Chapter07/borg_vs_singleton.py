# 实验单例模式的顶级类和子类是否共享状态
from singleton import Singleton
from borg import Borg
class SingletonA(Singleton):
    pass

class SingletonA1(SingletonA):
    pass


class SingletonB(Singleton):
    pass
    # _instance = "HAHA"
    # def __new__(cls, *args, **kwargs):
    #     print("SingletonB.__new__")
    #     return cls._instance

# 检查Borg模式的子类和父类是否共享状态
class ABorg(Borg):
    pass

class BBorg(Borg):
    pass

class A1Borg(ABorg):
    pass

if __name__ == "__main__":

    print("====Borg模式测试====")
    b0 = Borg()
    b = ABorg()
    b1 = A1Borg()
    bb = BBorg()
    b.x = 1000
    print(b == b1)
    print(bb == b1)

    print(b0.x)
    print(b1.x)
    print(bb.x)

    print("====单例模式测试====")
    a0 = Singleton()
    a = SingletonA()
    a1 = SingletonA1()

    sb = SingletonB()
    print(a.__dict__)
    print(sb.__dict__)

    a.x = 99
    print(a.__dict__)
    print(sb.__dict__)
    sb.x = 12312
    print(a == a0)
    print(a == a1)
    print(a == sb)
    print("a0.x=", a0.x)
    print("a1.x=", a1.x)
    print("sb.x=",sb.x)