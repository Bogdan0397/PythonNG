# def fact(n):
#     if n <= 1:
#         return 1
#
#     return n * fact(n - 1)
#
# print(fact(5))  # Output: 120

# def fact(n ,a=1):
#     if n <= 1:
#         return a
#
#     return fact(n - 1, a*n)
#
# print(fact(5))  # Output: 120

# ввод числа n
n = int(input())

# здесь задается функция fact_rec  (переменную n не менять!)
def fact_rec(n):
    if n<=1:
        return 1
    return fact_rec(n-1)*n

print(fact_rec(n))  # вывод факториала n