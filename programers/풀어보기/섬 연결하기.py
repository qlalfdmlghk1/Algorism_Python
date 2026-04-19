n,costs = 4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    answer = 0
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

    parents = [0] * (n+1)
    edges = []

    for i in range(1,n+1) :
        parents[i] = i

    for cost in costs :
        u,v,c = cost[0],cost[1],cost[2]
        edges.append((c,u,v))
    edges.sort()

    for edge in edges :
        cost,a,b = edge
        if findSet(parents,a) != findSet(parents,b) :
            union(parents,a,b)
            answer += cost

    return answer

print(solution(n,costs))