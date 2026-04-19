# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
#
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력.
from collections import defaultdict
nums = []
n = int(input())
nums = map(int,input().split())

dic = defaultdict()
for i in nums :
    dic[i] = 0

m = int(input())
new_nums = map(int,input().split())
for i in new_nums :
    if i in dic :
        print(1)
    else :
        print(0)