class Point:

    MAX_COORD = 1000
    MIN_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self,x,y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Access denied')
        return object.__getattribute__(self,item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError('Wrong name')
        return object.__setattr__(self,key,value)

    def __getattr__(self, item):
        """Виклик при зверненні до неіснуючого атрибути"""
        return False

    def __delattr__(self, item):
        object.__delattr__(self,item)


pt = Point(1,2)
del pt.x
print(pt.__dict__)
