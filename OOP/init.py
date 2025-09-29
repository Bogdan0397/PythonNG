class Point:
    color = "red"  # Class attribute
    circle = 3.14  # Class attribute

Point.type_tp = "2D"  # Adding a new class attribute

a = getattr(Point,'a', 'No such attribute')  # Safe way to get an attribute
print(a)
del Point.type_tp
print(hasattr(Point, 'type_tp'))  # Check if attribute exists