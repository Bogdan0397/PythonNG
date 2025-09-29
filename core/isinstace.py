a = [1,2,3,4,'hello','world',5.6,7.8,9.0]


p = sum(filter(lambda x: isinstance(x, (int,float)), a))
print(p)