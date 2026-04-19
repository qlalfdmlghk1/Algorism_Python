n,k,d = map(int,input().split())  # n: 상자의 개수, k: 규칙의 수, d: 도토리 개수

rules = []
for _ in range(k) :
    a,b,c = map(int,input().split())
    rules.append((a,b,c))

left = 1
right = n
answer = n

def check(n) :
    cnt = d
    for start,end,gap in rules :
        if start <= n :
            cnt -= ((min(end,n) - start) // gap+1)

    return cnt

while left <= right :
    mid = (left + right) // 2  # mid 번 박스까지의 도토리 개수 세면 어떻게 되나?
    if check(mid) <= 0:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)