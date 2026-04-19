t = int(input())
for _ in range(t) :
    n = int(input())
    candidates = []
    for i in range(n) :
        a,b = map(int, input().split())
        candidates.append((a,b))

    candidates.sort()

    top = 0
    result = 1

    for i in range(1, len(candidates)):
        if candidates[i][1] < candidates[top][1]:
            top = i
            result += 1

    print(result)
