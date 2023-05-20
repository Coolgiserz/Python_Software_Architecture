"""
原型模式：允许创建一个类的实例作为模版实例，通过复制或克隆原型来创建新的实例.

什么时候建议采用原型模式
"""
import copy
class Prototype(object):
    """
    实现了原型模式的类
    """
    def clone(self):
        """
        使用深拷贝实现对象的克隆。
        备注：若使用浅层拷贝，则所有的对象都是通过引用复制的，对复制出的实例的可变对象进行修改会导致另一个实例的相同对象
        :return:
        """
        return copy.deepcopy(self)

class Register(Prototype):
    def __init__(self, names=[]):
        self.names = names

class ShallowPrototype(object):
    def clone(self):
        return copy.copy(self)

class ShallowRegister(ShallowPrototype):
    def __init__(self, names=[]):
        self.names = names


if __name__ == "__main__":
    r1 = Register(names=["Mofei", "HQ"])
    r2 = r1.clone()
    print(r1 is r2)
    print(r1.names is r2.names)
    print(r1.names == r2.names)

    # 浅层拷贝
    sr1 = ShallowRegister(names=["XB","AJ"])
    sr2 = sr1.clone()
    sr1.names.append("hhh")
    print(sr2.names)
    print(id(sr1), id(sr2))
    print(sr1 is sr2)
    print(sr1.names is sr2.names)
    print(sr1.names == sr2.names)