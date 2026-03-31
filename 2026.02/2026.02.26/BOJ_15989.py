T = int(input())

for _ in range(T) : 
    N = int(input())
    dp = [0] * (N+1)
    dp[0] = 1

    for coin in [1,2,3] :
        for i in range(coin,N+1) :
            dp[i] += dp[i-coin]
    print(dp[N])