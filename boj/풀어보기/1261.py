from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(m) :
    graph.append(list(input()))

visited = [[0 for _ in range(n)] for _ in range(m)]

def bfs(r,c) :
    q = deque()
    q.append((r,c))
    dr,dc = [1,-1,0,0],[0,0,1,-1]
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < m :
