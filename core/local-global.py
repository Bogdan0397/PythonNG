# x = 0
#
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         print("Inner x:", x)  # Should print 2
#     inner()
#     print("Outer x:", x)      # Should print 2
#
# outer()
# print("Global x:", x)        # Should print 0


def counter(start = 0):
    def add():
        nonlocal start
        start += 1
        return start
    return add
# nonlocal start lives until counter() is alive
c1 = counter(10)
c2 = counter()
print(c1(), c2())  # Should print 11
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())# Should print 12