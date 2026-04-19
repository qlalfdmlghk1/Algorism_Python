n = int(input())
arr = list(map(int,input().split()))
dp = [a for a in arr]

for i in range(1,n) :
    for j in range(1,i+1) :
        if arr[i-j] < arr[i] :
            dp[i] = max(dp[i-j] + arr[i], dp[i])
# print(dp)
print(max(dp))