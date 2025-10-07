class Geom:
    name = 'Geom'

    def __init__(self,x1,x2,y1,y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2



class Rect(Geom):

    def __init__(self,x1,x2,y1,y2,fill='red'):
        super().__init__(x1,x2,y1,y2)
        self.__fill = fill



r = Rect(0,0,10,20)

print(r.__dict__)