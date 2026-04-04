import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[0] * (N+1)]
for _ in range(N) :
    row = list(map(int,input().split()))
    row.insert(0,0)
    graph.append(row)

dp = [[0 for _ in range(N+1)] for _ in range(N+1) ]
dp[0][0] = graph[0][0]

for i in range(1,N+1) :
    for j in range(1,N+1) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i][j]

for _ in range(M) :
    x1,y1,x2,y2 = map(int,input().split())

    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)