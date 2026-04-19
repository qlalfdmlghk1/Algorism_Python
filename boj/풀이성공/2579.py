n = int(input())
stair = []
for _ in range(n) :
    stair.append(int(input()))

dp = [0 for _ in range(n)]

dp[0] = stair[0]
if n > 1 :
    dp[1] = stair[0] + stair[1]
# dp[2] = max(dp[0] + stair[2], dp[1] + stair[2])

if n > 2 :
    for i in range(2,n) :
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n-1])