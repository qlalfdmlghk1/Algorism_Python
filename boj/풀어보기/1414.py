def findSet(a) :
    if a == parents[a] :
        return a
    else :
        parents[a] = findSet(parents[a])
        return parents[a]

def union(a,b) :
    aRoot = findSet(a)
    bRoot = findSet(b)
    if aRoot != bRoot :
        if aRoot < bRoot :
            parents[bRoot] = aRoot
        else :
            parents[aRoot] = bRoot

n = int(input())
edges = [[] for _ in range(n)]
parents = [0] * (n+1)
for i in range(n+1) :
    parents[i] = i

total = 0
graph = []
for _ in range(n) :
    graph.append(list(input()))

edges = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            edges.append((0, i+1, j+1))
        else:
            if ord('a') <= ord(graph[i][j]) <= ord('z'):
                edges.append((ord(graph[i][j]) - ord('a')+1, i+1, j+1))
                total += (ord(graph[i][j]) - ord('a') + 1)
            elif ord('A') <= ord(graph[i][j]) <= ord('Z'):
                edges.append((ord(graph[i][j]) - ord('A') + 27, i+1, j+1))
                total += (ord(graph[i][j]) - ord('A') + 27)

edges.sort()
for e in edges :
    len, a, b = e
    if len == 0 :
        continue
    if findSet(a) != findSet(b) :
        union(a, b)
        total -= len
    else :
        continue

result = True
for i in range(1,n+1) :
    if findSet(i) != 1 :
        result = False

if result :
    print(total)
else :
    print(-1)