# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Before the function call')
#         res = func(*args, **kwargs)
#         print('After the function call')
#         return res
#     return wrapper
#
#
# @func_decorator
# def some_function(title,slug):
#     return f'{title},{slug}'
#
#
#
# print(some_function('My Title','my-title'))

def func_show(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
    return wrapper


def get_sq(width, height):
    return width * height

func = func_show(get_sq)
res = func(5, 10)







