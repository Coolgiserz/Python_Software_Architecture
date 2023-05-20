class Proxy(object):
    # def __new__(cls, *args, **kwargs):
    #     instance = object.__new__(cls)
    #     return instance

    def __init__(self, instance):
        self.instance =  instance

    def good(self):
        print(f"good {self.__class__}")
    def __getattr__(self, item):
        """
        重载__getattr__来重定向方法访问权
        规定当在Proxy找不到item时,模块应该到哪里寻找item
        :param item:
        :return:
        """
        return getattr(self.instance, item)

class CoreClass(object):
    def good(self):
        print(f"good {self.__class__}")
    def hello(self, msg=""):
        print("good", msg)

if __name__ == "__main__":
    p = Proxy(CoreClass())
    p.good()
    p.hello("proxy pattern")