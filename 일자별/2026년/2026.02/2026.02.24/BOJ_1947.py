N = int(input())
dp = [0] * (N+1)
dp[2] = 1
dp[3] = 2

dp[N] = (N-1) * dp(N-1) + {dp[N-2] + (N-2) * dp[]}