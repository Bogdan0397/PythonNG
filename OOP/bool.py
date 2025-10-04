class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x*self.x + self.y*self.y

    def __bool__(self):
        return self.x == self.y

p1 = Point(1,2)
p2 = Point(1,2)

print(bool(p1))