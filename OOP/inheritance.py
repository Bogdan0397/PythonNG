class Geom:
    name = 'Geom'

    def set_coords(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.draw()

        
class Line(Geom):
    def draw(self):
        print('Draw line')


class Rect(Geom):
    def draw(self):
        print('Draw Rect')



l = Line()
r = Rect()
l.set_coords(1,2,3,4)
r.set_coords(6,7,8,9)


