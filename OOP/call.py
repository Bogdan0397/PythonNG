class Point:

    def __init__(self):
        self.__counter = 0


    def __call__(self, step=0, *args, **kwargs):
        print('call')
        self.__counter += step
        return self.__counter


p1 = Point()
p2 = Point()

print(p1(1))
print(p2(5))

class Redactor:
    def __init__(self,chars):
        self.__chars = chars


    def __call__(self, *args, **kwargs):
        if not isinstance(args[0],str):
            raise ValueError('Must be string')

        return args[0].strip(self.__chars)



s = Redactor('!,. ')
print(s(' Hello world !..'))

class Wrapper:
    def __init__(self,func):
        self.__func = func


    def __call__(self,w,h,step=5, *args, **kwargs):
        """Change function logic without changing function"""
        print('decorated func')
        return self.__func(w,h) + step



@Wrapper
def count_square(w,h):
    return w*h


print(count_square(2,2))