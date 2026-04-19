import sys
input = sys.stdin.readline

n,m = map(int, input().split())

parents = [0] * (n+1)
for i in range(1,n+1) :
    parents[i] = i

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
for _ in range(m) :
    a,b,c = map(int,input().split())
    edges.append((a,b,c))
edges.sort(key=lambda x:x[2])

last,result = 0,0
for edge in edges :
    a,b,cost = edge
    if findSet(parents,a) != findSet(parents,b) :
        last = cost
        union(parents,a,b)
        result += cost
print(result - last)

