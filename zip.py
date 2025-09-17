a = [1,2,3,4,5]
b = [6,7,8,9,10,11,12]
z = list(zip(a,b))
t1, t2 = zip(*z)
print(z)
print(t1)
print(t2)

