n, r, q = map(int,input().split())

# 그냥 DFS 임?
graph = []
graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
cnt = [1] * (n+1)
visited[r] = True

def dfs(start) :
    if not graph[start] :
        return 1

    for nex in graph[start] :
        if not visited[nex] :
            # print(start, cnt, nex)
            visited[nex] = True
            cnt[start] += dfs(nex)
    return cnt[start]

dfs(r)

for _ in range(q) :
    s = int(input())
    print(cnt[s])



# 유니온 파인드 인가?
# n,r,q = map(int,input().split())
# parents = [0] * (n+1)
#
# def findSet(parents,a) :
#     if parents[a] != a :
#         parents[a] = findSet(parents,parents[a])
#     return parents[a]
#
# def union(parents,a,b) :
#     aRoot = findSet(parents,a)
#     bRoot = findSet(parents,b)
#     if aRoot <= bRoot :
#         parents[bRoot] = aRoot
#     else :
#         parents[aRoot] = bRoot
#
# for i in range(1,n+1) :
#     parents[i] = i
#
# for i in range(n-1) :
#     u,v = map(int,input().split())
#     union(parents,u,v)
#
# findSet(parents,r)
# for i in range(q) :
#     a = int(input())
    # findSet(parents,a)
