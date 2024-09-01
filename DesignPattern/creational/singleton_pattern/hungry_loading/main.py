
from singleton_module import config, _SingletonModule

a = config
b = config
c = _SingletonModule()
print(a is b)
print(c is a)