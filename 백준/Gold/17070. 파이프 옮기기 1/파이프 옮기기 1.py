N = int(input())

graph = []
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
for _ in range(N) :
    graph.append(list(map(int,input().split())))

dp[0][1][0] = 1

for i in range(N) :
    for j in range(2,N) : 
        if graph[i][j] == 0 :
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 가로 

            if i > 0 :
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] # 세로

                if graph[i-1][j] == 0 and graph[i][j-1] == 0 :
                    dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2] # 세로

print(sum(dp[N-1][N-1]))