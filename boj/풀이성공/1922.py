n = int(input())
m = int(input())

parents = [i for i in range(n+1)]
edges = []
result = 0

def findSet(parents,a) :
    if parents[a] != a :
        parents[a] = findSet(parents,parents[a])
    return parents[a]

def union(parents,a,b) :
    aRoot = findSet(parents,a)
    bRoot = findSet(parents,b)
    if aRoot <= bRoot :
        parents[bRoot] = aRoot
    else :
        parents[aRoot] = bRoot

for _ in range(m) :
    a,b,cost = map(int,input().split())
    edges.append((a,b,cost))
edges.sort(key=lambda x : x[2])

for edge in edges :
    a,b,cost = edge
    if findSet(parents,a) != findSet(parents,b) :
        union(parents,a,b)
        result += cost

print(result)