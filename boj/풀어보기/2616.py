n = int(input())
trains = [0] + list(map(int,input().split()))
max_train = int(input())

dp = [[0 for _ in range(n+1)] for _ in range(4)]

for i in range(1,4) :
    for j in range(max_train * i, n+1) :
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-max_train] + sum(trains[j-max_train+1:j+1]))

print(dp[3][n])