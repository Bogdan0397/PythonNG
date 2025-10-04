class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))

p1 = Point(2,3)
p2 = Point(2,3)
d = {}
d[p1] = 1
d[p2] = 2
print(p1,p2)
print(d) # p1 remain as a first key, and rewrite its value to 2

# <__main__.Point object at 0x000002D148336F90> <__main__.Point object at 0x000002D1485C5090>
# {<__main__.Point object at 0x000002D148336F90>: 2}