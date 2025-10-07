class Vector():
    def __str__(self):
        return " ".join(map(str,self))

print(issubclass(int,object))

l = Vector([1,2,3])

print(l)
