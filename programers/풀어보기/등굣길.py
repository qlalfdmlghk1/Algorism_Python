m,n,puddles	= 4,3,[[2, 2]]
dp = [[0 for i in range(m)] for i in range(n)]
pud = {}
dp[0][0] = 1
for x,y in puddles :
    pud[(x,y)] = True

for i in range(n) :
    for j in range(m) :
        print(i,j)
        print(dp)
        if (i+1,j+1) in pud :
            continue
        else :
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0 :
                dp[i][j] = dp[i][j - 1]
            elif j == 0 :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n-1][m-1] % 1000000007)


