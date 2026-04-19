n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]  # i로 끝나는 수

for i in range(n) :
    for j in range(10) :
        if j == 0 :
            dp[i][j] = 1
        else :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
# print(dp)
print(sum(dp[n-1])%10007)