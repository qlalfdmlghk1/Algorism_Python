n = int(input())
dp = [0] * (n+1)
dp[2] = 1
dp[3] = 2
dp[4] = 9
for i in range(5,n+1) :
    dp[i] = (i-1) * (dp[n-1] + dp[n-2]) % 1000000000
print(dp[n])