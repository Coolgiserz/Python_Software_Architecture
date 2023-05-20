"""
状态模式：
意图：当对象的状态改变时，改变其行为（像变了一个类似的）
对象的行为依赖于其状态

举例理解：
   1）人在不同精神状态时，行为举止会有很大不同，如意气风发时行为大方、积极沟通；闷闷不乐时孤僻少言，能力发挥失常；
   2）狼人平时像人，圆月之夜状态改变，行为变得凶残

经典模型：
   有限状态机（finite-state machine：机器总共可能有有限的N个状态，在任意时刻具有一个状态，状态之间可以进行转移。

什么时候使用状态模式？

Python中实现状态模式的优雅方法？
__class__属性，通过类实例的__class__属性可以获取到类

"""
import random


class HumanState(object):
    """
    人类状态基类
    """
    # 当前状态可以切换到的一组合法状态
    next_states = []
    # 可以切换到的随机合法状态
    random_states = []
    def __init__(self):
        self.index = 0

    def __str__(self):
        return self.__class__.__name__

    def __iter__(self):
        return self

    def change(self):
        self.__next__()

    def set(self, state):
        """
        1. 判断当前状态是否可以转变到state状态
        2.1 若可以，进行状态转移
        2.2 若不可以，进行提醒，抛出异常
        :param state:
        :return:
        """
        print("Set state", state)
        if self.index < len(self.next_states):
            if state in self.next_states:
                self.index = self.next_states.index(state)
                self.__class__ = eval(state)
                return self.__class__
            else:
                raise Exception(f"illegal transition from {self.__class__} to {eval(state)}")
        else:
            self.index = 0
            if state in self.random_states:
                self.__class__ = eval(state)
                return self.__class__


    def __next__(self):
        """
        转移到下一个状态
        注意：状态数是有限的
        :return:
        """
        # print("Next State")
        # 若可以转移到下一个合法状态
        if self.index < len(self.next_states):
            self.__class__ = eval(self.next_states[self.index])
            self.index += 1
            return self.__class__
        else:
            # 若已经遍历完可顺序转移的状态，则随机转移状态
            self.index = 0
            if len(self.random_states):
                state = random.choice(self.random_states)
                self.__class__ = eval(state)
                return self.__class__
            else:
                raise StopIteration

class HumanYoung(HumanState):
    """
    年轻人
    """
    next_states = ["HumanMiddle"]
    random_states = ["HumanMiddle", "HumanOptim", "HumanPassive"]


class HumanMiddle(HumanState):
    """
    中年人
    """
    next_states = ["HumanOld"]
    random_states = ["HumanSuccess", "HumanFail", "HumanPassive"]

class HumanOld(HumanState):
    """
    老年人
    """
    random_states = ["HumanSuccess", "HumanFail"]

class HumanOptim(HumanState):
    random_states = ["HumanSuccess", "HumanPassive", "HumanFail"]


class HumanPassive(HumanState):
    next_states = ["HumanFail"]


class HumanSuccess(HumanState):
    next_states = ["HumanYoung"]
    random_states = ["HumanSuccess", "HumanFail"]

class HumanFail(HumanState):
    next_states = ["HumanOld"]

class Human(object):
    def __init__(self, name):
        self.name = name
        self.state = HumanYoung()

    def change(self, state=None):
        """
        改变状态
        :param state:
        :return:
        """
        if state is None:
            return self.state.change()
        else:
            return self.state.set(state)

    def __str__(self):
        return str(self.state)


if __name__ == "__main__":
    h = HumanState()
    print(h)
    print(HumanState)
    print(h.__class__)

    hiter = iter(h)

    # next(hiter)
    print("This is a Human")
    human = Human(name="Julia")
    print(human)
    human.change(state="HumanOld")
    print(human)
    human.change(state="HumanOld")
    print(human)
    #
    # print("iter Human state")
    # import itertools
    # print(human)
    # for s in itertools.islice(human.state, 10):
    #     print(s)