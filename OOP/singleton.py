class Point:

    __Singleton = None

    def __new__(cls, *args, **kwargs):
        if cls.__Singleton is None:
            cls.__Singleton = super().__new__(cls)
            return cls.__Singleton

        return cls.__Singleton

    def __del__(self):
        Point.__Singleton = None

    def __init__(self, x, y):
        print("__init__" + str(self))
        self.x = x
        self.y = y

    @classmethod
    def validate(cls):
        if cls.__Singleton is None:
            return False
        return True


p1 = Point(1,2)
p2 = Point(3,4)

