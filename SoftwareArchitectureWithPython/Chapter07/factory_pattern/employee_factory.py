"""
工厂模式：通过一个Factory类关联整个类家族，创建类家族层次结构中的任意类

"""
from employee import Employee, Engineer, Accountant, Admin
class EmployeeFactory(object):
    @classmethod
    def create(cls, name, *args):
        """
        工厂方法通常声明为classmethod，该方式使工厂方法可以通过类的命名空间直接调用
        :param name:
        :param args:
        :return:
        """
        name = name.lower().strip()
        if name == "engineer":
            return Engineer(*args)
        elif name == "accountant":
            return Accountant(*args)
        elif name == "admin":
            return Admin(*args)

if __name__ == "__main__":
    factory = EmployeeFactory()
    print(factory.create("engineer", "Mofei", 22, "F"))
    print(factory.create("manager", "HuQ", 35, "M"))
    print(factory.create("admin", "LS", 40, "F"))
    print(factory.create("accountant", "RY", 28, "F"))



