k, n = map(int, input().split())  # k : 가지고 있는 랜선 수, n : 필요한 랜선 수
lens = []

for _ in range(k) :
    lens.append(int(input()))

ans = 0
left, right = 1,max(lens)
while left <= right :
    mid = (left+right) // 2
    cnt = 0
    for l in lens :
        cnt += l // mid

    if cnt >= n :
        ans = max(ans,mid)
        left = mid + 1
    else :
        right = mid - 1

print(ans)