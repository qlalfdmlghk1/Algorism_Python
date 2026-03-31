N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

#dp[r][c][d] : 파이프 머리가 (r,c)에 방향 d로 놓이는 경우의 수
# d=0 : 가로, d=1 : 대각선, d=2 : 세로, 
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1 

for r in range(N) :
    for c in range(2,N) :
        if graph[r][c] == 1 :
            continue
            
        # 가로: 이전이 가로 or 대각선
        dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][1]
        # 세로: 이전이 세로 or 대각선
        if r > 0:
            dp[r][c][2] = dp[r - 1][c][2] + dp[r - 1][c][1]
        # 대각선: 이전이 가로, 세로, 대각선 모두 가능 + 3칸 검사
        if r > 0 and graph[r - 1][c] == 0 and graph[r][c - 1] == 0:
            dp[r][c][1] = dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]

print(sum(dp[N-1][N-1]))

