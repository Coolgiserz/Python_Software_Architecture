from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):
    """雇员"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.__class__} - {self.name}, {self.age}, {self.gender}"


class Engineer(Employee):
    def get_role(self):
        return "engineering"

class Accountant(Employee):
    def get_role(self):
        return "accountant"

class Admin(Employee):
    def get_role(self):
        return "administration"

