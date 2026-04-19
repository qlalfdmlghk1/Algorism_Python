n = int(input())
dp = [0] * (n+1)
stair = [0] * (n+1)
for i in range(n) :
    stair[i+1] = int(input())
    if i == 0 :
        dp[i+1] = stair[i+1]
    elif i == 1 :
        dp[i+1] = stair[i+1]+stair[i]

for i in range(3,n+1) :
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
print(dp[-1])