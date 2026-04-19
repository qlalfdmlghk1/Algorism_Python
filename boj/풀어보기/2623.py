from collections import deque

n,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
prev = [0] * (n+1)
answer = []

for _ in range(c) :
    link = list(map(int,input().split()))
    length = link.pop(0)
    for i in range(1,length) :
        a = link[i-1]
        b = link[i]
        graph[a].append(b)
        prev[b] += 1

q = deque()
for i in range(1,n+1) :
    if prev[i] == 0 :
        q.append(i)

order = []

while q :
    cur = q.popleft()
    order.append(cur)
    for nex in graph[cur] :
        prev[nex] -= 1
        if prev[nex] == 0 :
            q.append(nex)

if len(order) != n :
    print(0)
else :
    print(*order, sep="\n")
