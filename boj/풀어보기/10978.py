t = int(input())

dp = [0] * (21)
dp[2] = 1
for i in range(3, 21):
    dp[i] = (i-1) * (dp[i-1] + dp[i-2])

for _ in range(t) :
    n = int(input())
    print(dp[n])