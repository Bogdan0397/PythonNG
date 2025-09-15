b = map(int,['1','2','3'])
print(list(b))
c = map(str,[1,2,3])
print(list(c))


d = map(lambda s: list(s.lower()), ['Hello', 'World'])
print(list(d))