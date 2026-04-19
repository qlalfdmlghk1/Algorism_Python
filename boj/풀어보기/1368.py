n = int(input())
well = []
graph = []

def findSet(parents, a) :
    if parents[a] != a :
        parents[a] = findSet(parents, parents[a])
    return parents[a]

def union(parents, a, b) :
    aRoot = findSet(parents,a)
    bRoot = findSet(parents,b)
    if aRoot < bRoot :
        parents[bRoot] = aRoot
    else :
        parents[aRoot] = bRoot

parents = [0] * (n+1)
edges = []
result = 0

for _ in range(n) :
    well.append(int(input()))
for _ in range(n) :
    graph.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(n):
        if i != j :
            cost, a, b = graph[i][j], i, j
            edges.append((cost,a,b))


for i in range(n):
    edges.append((well[i], i, i))

edges.sort()
print(edges)

for i in range(n+1) :
    parents[i] = i

for edge in edges :
    cost,a,b = edge
    if findSet(parents,a) != findSet(parents,b) :
        union(parents,a,b)
        result += cost

print(result)