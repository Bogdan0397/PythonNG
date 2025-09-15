a = [1,2,3,4,5,6,7,8,9,10]


def is_prost(x):
    d = x-1
    if d < 0:
        return False

    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True

b = filter(is_prost, a)
print(list(b))