# l = input().split()
# res = [ list((l[x], int(l[x+1]))) for x in range(0,len(l)-1,2)]
# print(res)
#
#
#
# N = int(input())
#
# res = [[ 1 if j==i else 0 for j in range(N)] for i in range(N)]
#
# for i in res:
#     print(*i)
import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

res = [x for i in lst_in[::-1] for x in i[::-1]]

print(' '.join(map(str, res)))

