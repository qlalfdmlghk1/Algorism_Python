import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[0 for _ in range(n+1)]]
sum_square = [[0 for _ in range(n+1)]]

for _ in range(n) :
    arr = list(map(int,input().split()))
    arr.insert(0,0)
    graph.append(arr)
    sum_square.append(arr)
# print(sum_square)

for r in range(1,n+1) :
    for c in range(1,n+1):
        sum_square[r][c] += (sum_square[r-1][c] + sum_square[r][c-1] - sum_square[r-1][c-1])
# print(sum_square)

for _ in range(m) :
    x1,y1,x2,y2 = map(int,input().split())
    answer = sum_square[x2][y2] - sum_square[x1-1][y2] - sum_square[x2][y1-1] + sum_square[x1-1][y1-1]
    print(answer)
