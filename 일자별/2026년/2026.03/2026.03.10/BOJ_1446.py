N,D = map(int,input().split())  # 지름길 개수, 고속도로 길이

dp = [i for i in range(D+1)]

route = []
for _ in range(N) : 
    s,e,d = map(int,input().split())
    if s <= D and e <= D :
        route.append((s,e,d))

route.sort(key = lambda x : x[0])

for i in range(D+1) :
    if i > 0 :
        dp[i] = min(dp[i], dp[i-1] + 1)

    for s,e,d in route :
        if s == i :
            dp[e] = min(dp[e],dp[i]+d)

print(dp[D])


