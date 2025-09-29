pole = [
    ['#', '*', '*', '*', '#'],
    ['#', '#', '#', '#', '#'],
    ['*', '*', '*', '*', '#'],
    ['#', '#', '*', '*', '*'],
    ['#', '#', '*', '#', '#'],
]

N = len(pole)

def set_zeros(p, i,j, sz):
    if p[i][j] != '*':
        return
    p[i][j] = '@'

    if i-1 >= 0 and p[i-1][j] == '*':
        set_zeros(p, i-1, j, sz)
    if i+1 < sz and p[i+1][j] == '*':
        set_zeros(p, i+1, j, sz)
    if j-1 >= 0 and p[i][j-1] == '*':
        set_zeros(p, i, j-1, sz)
    if j+1 < sz and p[i][j+1] == '*':
        set_zeros(p, i , j+1 ,sz)



set_zeros(pole, 2, 2, N)

for i in pole:
    print(i)
