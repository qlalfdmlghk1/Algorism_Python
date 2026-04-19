# import sys
# input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n)]
# dp = [[0 for _ in range(m)] for _ in range(n)]
dp = [[] for _ in range(n)]

for i in range(n) :
    line = input()
    for j in line :
        graph[i].append(int(j))
        dp[i].append(int(j))


for i in range(1,n) :
    for j in range(1,m) :
        if graph[i][j] == 1 :
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        else :
            dp[i][j] = 0

result = 0

for i in range(n) :
    for j in range(m) :
        if dp[i][j] > result :
            result = dp[i][j]
print(result * result)