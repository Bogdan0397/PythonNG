class Point:
    color = "red"  # Class attribute
    circle = 3.14  # Class attribute

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("Object deleted")

    def set_coords(self):
        print(self.x, self.y)


p = Point(1,2)
p.set_coords()