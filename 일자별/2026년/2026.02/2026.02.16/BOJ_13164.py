N,K = map(int,input().split())
children = list(map(int,input().split()))

diffs = []

for i in range(1,N) :
    diffs.append(children[i]-children[i-1])

diffs.sort()

print(sum(diffs[:N-K]))

# nCk 하기엔 n <= 300,000, 1<=k<=n 여서 단순 조합은 안되고
# 이분탐색?