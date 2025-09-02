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
#
# def set_reducer(inp):
#
#
#
#     return [1 if inp.count(x) == 1 else inp.count(x) for x in set(inp)]
#
# print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))
# def set_reducer(input):
#
#     counter = 1
#     a = []
#     for i in range(len(input)-1):
#         if input[i]==input[i+1]:
#             counter +=1
#         else:
#             a.append(counter)
#             counter = 1
#
#     a.append(counter)
#
#
#
#     if len(a) == 1:
#          return a[0]
#     else:
#         return set_reducer(a)
#
# print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))

l = [1,2,3,4,5,6,7,8,9]

print(sorted(l))