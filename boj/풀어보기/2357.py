import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for _ in range(n) :
    arr.append(int(input()))

for _ in range(m) :
    a,b = map(int,input().split())
    print(min(arr[a-1:b]), max(arr[a-1:b]))