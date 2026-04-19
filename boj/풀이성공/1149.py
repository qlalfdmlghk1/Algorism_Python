n = int(input())
grid = []
for _ in range(n) :
    grid.append((list(map(int,input().split()))))

dp = [[0,0,0] for _ in range(n)]
dp[0][0] = grid[0][0]
dp[0][1] = grid[0][1]
dp[0][2] = grid[0][2]
# print(dp)

for i in range(1,n) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + grid[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + grid[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + grid[i][2]
print(min(dp[n-1]))

