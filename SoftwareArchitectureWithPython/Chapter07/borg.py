"""
Borg模式

单例模式的目的、意义：
   我们希望所有实例初始化时具有单一的、相同/共享的状态
   实例是否完全相同不是最本质的，确保特定内存中只有一个实例存在的技术只是实现上述要求的一种方法

Borg模式：
1）对比单例模式的好处：不需要满足内存中只存在单个实例的需求，在复杂系统（存在竞争条件、使用多线程等）中容易实现所有实例共享状态
2）允许从顶级类到子类共享相同的状态；单例的每个子类回创建自己的状态
"""
class Borg(object):
    """
    注意：Borg模式不是单例模式
    """
    __shared_dict = {}
    def __init__(self):
        # 保证所有子类共享相同的状态
        self.__dict__ = self.__shared_dict



class IBorg(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.state = "iborg"
    def __str__(self):
        return self.state
# 实验单例模式的顶级类和子类是否共享状态
from singleton import Singleton
class SingletonA(Singleton):
    pass

class SingletonA1(SingletonA):
    pass

class SingletonA2(SingletonA):
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
    # b1 = Borg()
    # b2 = IBorg()
    # print(b1, b2)
    # print(b1.__dict__, b2.__dict__)
    #
    # b1.state = "666"
    # print(b1, b2)
    # print(b1.__dict__, b2.__dict__)
    #
    # b2.state = "99999"
    # print(b1, b2)
    # print(b1.__dict__, b2.__dict__)
    # print(b1 == b2)
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
    a2 = SingletonA2()

    sb = SingletonB()

    a.x = 99
    print(a == a0)
    print(a == a1)
    print(a1 == a2)
    print(a == sb)
    print(a2.x) # 会报错，
    print(a1.x) # 会报错，
    print(sb.x)