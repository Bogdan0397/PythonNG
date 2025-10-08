class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2(Point):
    __slots__ = ('z')
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

pt = Point2(10,20,25)
pt.z = 25
print(pt)