import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

m = int(input())
min_num = min(arr)

for _ in range(m) :
    query = list(map(int,input().split()))
    if query[0] == 1 :
        arr[query[1]-1] = query[2]
        min_num = min(arr)
    else :
        print(arr.index(min_num)+1)