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
        nex = cur + mid
        if h >= nex :
            cnt += 1 
            cur = h
    
    if cnt >= C : 
        left = mid + 1 
    else :
        right = mid - 1
    print(left,right)
print(right)