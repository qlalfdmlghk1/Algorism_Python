n = int(input())
week = []
for _ in range(n) :
    t,p = map(int, input().split())
    week.append((t,p))

# 무슨 알고리즘이지?  ->  DP 인가봐

dp = [0 for i in range(n+1)]

for i in range(n) :
    for j in range(i+week[i][0], n+1) :
        if dp[j] < dp[i] + week[i][1] :
            dp[j] = dp[i] + week[i][1]
print(dp[-1])