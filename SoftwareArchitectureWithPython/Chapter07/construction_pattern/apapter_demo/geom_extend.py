"""
适配器模式示例
"""
class Polygon(object):
    """多边形类"""
    def __init__(self, *sides):
        """
        初始化
        :param sides: 边长
        """
        self.sides = sides

    def perimeter(self):
        """周长"""
        return sum(self.sides)

    def is_valid(self):
        raise NotImplementedError

    def is_regular(self):
        """多边形是否规则：边长是否都相等"""
        side = self.sides[0]
        return all([x == side for x in self.sides[1:]])

    def area(self):
        raise NotImplementedError

class Triangle(Polygon):
    pass

def Rectangle(Polygon):
    pass
