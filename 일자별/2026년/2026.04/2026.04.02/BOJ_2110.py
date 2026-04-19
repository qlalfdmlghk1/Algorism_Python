N,C = map(int,input().split())
houses = []

for _ in range(N) :
    houses.append(int(input()))
houses.sort()

left,right = 1,houses[-1] - houses[0]
while left <= right :
    cur = houses[0]
    mid = (left + right) // 2
    cnt = 1
    for h in houses[1:] :
        if cur + mid <= h :
            cnt += 1
            cur = h
    print(left,right,cnt)
    if cnt >= C :
        left = mid + 1 
    else :
        right = mid - 1
print(right)