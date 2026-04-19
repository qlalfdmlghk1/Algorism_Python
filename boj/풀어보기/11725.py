n = int(input())

parents = [0] * (n+1)
for i in range(n+1) :
    parents[i] = i

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


for _ in range(n-1) :
    a,b = map(int,input().split())
    union(parents,a,b)

print(parents)