# d = [[1,2,3,4],
#      [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]]
#
# for i in range(len(d)):
#     for j in range(i+1,len(d[i])):
#         d[i][j], d[j][i] = d[j][i], d[i][j]
#
#
# d.index()

s = (x for x in range(10) if x%2 == 0)
print(list(s))