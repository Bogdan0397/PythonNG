class Point:
    def __init__(self, x, y):
        self.__x = x  # Private attribute
        self.__y = y  # Private attribute

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__check_value(x)
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__check_value(y)
        self.__y = y

    @classmethod
    def __check_value(cls,x):
        if x <= 0:
            raise ValueError("Coordinates must be non-negative")


p1 = Point(1,2)
p1.x = 2
p1.y = 4
print(p1.x)
print(p1.y)