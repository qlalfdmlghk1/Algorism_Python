from collections import deque
t = int(input())
for _ in range(t) :
    n = int(input())
    parents = [[] for _ in range(n+1)]

    for i in range(n-1) :
        a,b = map(int, input().split())
        parents[b].append(a)

    x,y = map(int, input().split())
    q = deque()
    q.append(y)
    parents_y = {}
    while q:
        cur = q.popleft()
        parents_y[cur] = True
        if parents[cur]  :
            q.append(parents[cur][0])

    q = deque()
    q.append(x)
    while q:
        cur = q.popleft()
        if cur in parents_y :
            print(cur)
            break
        if parents[cur] :
            q.append(parents[cur][0])