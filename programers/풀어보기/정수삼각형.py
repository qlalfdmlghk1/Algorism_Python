triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
dp = triangle
n = len(triangle)
for i in range(1,n) :
    for j in range(i+1) :
        if j == 0 :
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i :
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else :
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
print(dp)
print(max(dp[n-1]))

