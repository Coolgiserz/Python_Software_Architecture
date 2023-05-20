"""
适配器模式：将特定接口的现有实现包装或调整到客户端期望的另一个接口中
现实案例：数据线转换头、视频输出转接头（hdmi）、电源转换器
适配器：包装器

实现思路：
1. 类适配器
 通过继承进行适配
2. 对象适配器
 通过组合（所要适配类的实例）进行适配

 两种思路对比（灵活度、代码量）
"""

if __name__ == "__main__":
    salarys = [("admin", 2333), ("manager", 213123)]
    salary_dict = dict(salarys)
    print(salary_dict)

    print(dict(qwe=2, asda=23))