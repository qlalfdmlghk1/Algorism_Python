N,C = map(int,input().split())
houses = []
for _ in range(N) :
    houses.append(int(input()))
houses.sort()

left,right = 1,houses[-1] - houses[0]


while left <= right :
    mid = (left + right) // 2  # 공유기 사이의 최소 거리
    cnt = 1 # 찻반쩨 집은 무조건 설치
    cur = houses[0]
    for h in houses[1:] :
        if abs(h - cur) >= mid :
            cnt += 1 # 설치
            cur = h
    if cnt >= C :
        left = mid + 1
    else :
        right = mid - 1

print(right)