n = int(input())

parents = [0] * (n+1)
for i in range(1,n+1) :
    parents[i] = i

graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

def findSet(parents,a) :
    if parents[a] != a :
        parents[a] = findSet(parents,parents[a])
    return parents[a]

def union(parents,a,b) :
    aRoot = findSet(parents,a)
    bRoot = findSet(parents,b)
    if aRoot < bRoot :
        parents[bRoot] = aRoot
    else :
        parents[aRoot] = bRoot

edges = []
for i in range(n-1) :
    for j in range(i+1,n) :
        edges.append((i,j,graph[i][j]))
        edges.append((j,i, graph[j][i]))
edges.sort(key=lambda x:x[2])

result = 0
for edge in edges :
    a,b,cost = edge
    if findSet(parents,a) != findSet(parents,b) :
        union(parents,a,b)
        result += cost
print(result)