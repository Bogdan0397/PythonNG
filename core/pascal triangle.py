
def pascal_triangle(n):
    P = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = P[i-1][j-1] + P[i-1][j]

        P.append(row)

    for i in P:
        print(str(i).center(20))

pascal_triangle(5)


