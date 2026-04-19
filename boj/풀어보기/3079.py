n,m = map(int, input().split())
check = []
for _ in range(n) :
    check.append(int(input()))

start, end = min(check), max(check) * m
answer = end

while start <= end :
    total = 0
    mid = (start + end) // 2

    for i in range(n) :
        total += mid // check[i]

    if total >= m :
        end = mid - 1
        answer = min(mid, answer)

    else :
        start = mid + 1

print(answer)
