from collections import deque

a,b = map(int,input().split())
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m) :
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start,end) :

    q = deque()
    q.append((start,0))
    visited[start] = True
    while q :
        cur,cur_cnt = q.popleft()
        if cur == end :
            return cur_cnt
        for nex in graph[cur] :
            if not visited[nex] :
                nex_cnt = cur_cnt + 1
                q.append((nex,nex_cnt))
                visited[nex] = True
    return -1

print(bfs(a,b))