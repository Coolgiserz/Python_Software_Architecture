"""
返回随机数据、模拟数据

扩展：
 Faker库
"""
import random
import string

from schematics import Model
from schematics.types import StringType, BaseType, IntType, DateTimeType


class AgeType(IntType):
    def __init__(self, **kwargs):
        kwargs["default"] = 18
        IntType.__init__(self, **kwargs)
    def to_primitive(self, value, context=None):
        return random.randrange(18, 25)

class NameType(StringType):
    """自定义类型"""
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase)-set(vowels))
    def __init__(self, **kwargs):
        kwargs["default"] = ""
        StringType.__init__(self, **kwargs)

    def get_name(self):
        """
        名字生成器
        :return:
        """
        items = [""]*4
        items[0] = random.choice(self.consonants)
        items[2] = random.choice(self.consonants)
        for i in (1, 3):
            items[i] = random.choice(self.vowels)
        return "".join(items).capitalize()

    def to_primitive(self, value, context=None):
        return self.get_name()

class GenderType(BaseType):
    def __init__(self, **kwargs):
        kwargs["choices"] = ["male", "female"]
        kwargs["default"] = "male"
        BaseType.__init__(self, **kwargs)

class ConditionType(StringType):
    """
    健康状况
    """
    def __init__(self, **kwargs):
        kwargs["default"] = "cardiac" # 心脏病
        StringType.__init__(self, **kwargs)

    def to_primitive(self, value, context=None):
        return random.choice((
            "cardiac",
            "respiratory", # 呼吸疾病
            "nasal",    # 鼻道
            "gynec",    # 妇科
            "urinal",   # 尿
            "lungs",    # 肺
            "thyroid",  # 甲状腺
            "tumour"    # 肿瘤

        ))

import itertools
class BloodGroupType(StringType):
    def __init__(self, **kwargs):
        kwargs["default"] = "AB+"
        StringType.__init__(self, **kwargs)

    def to_primitive(self, value, context=None):
        return "".join(random.choice(list(itertools.product(["AB", "A", "O", "B"],["+", "-"]))))
class Person(Model):
    name = NameType()
    age = AgeType()
    gender = GenderType()

class Patient(Model):
    name = NameType()
    age = AgeType()
    gender = GenderType()
    healthy = ConditionType()
    blood = BloodGroupType()
    last_visit = DateTimeType(default="2000-01-01T13:00:00")

# for i in range(100):
#     print(Patient.get_mock_object().to_primitive())
# print(Person.get_mock_object().to_primitive())
#     print(Person.get_mock_object().to_native())
# print(Person.get_mock_object().to_primitive())


from max_subserial import timer
# map方法，不需要循环即可创建处理可迭代对象 map(function, iterable[, iterable1, iterable2,..., iterableN])
# Python's map(): Processing Iterables Without a Loop： https://realpython.com/python-map-function/
N = 100000
with timer():
    # lst = []
    patients = map(lambda x: Patient.get_mock_object().to_primitive(), range(N))
    lst = list(patients)

with timer():
    lst1 = []
    for i in range(N):
        lst1.append(Patient.get_mock_object().to_primitive())