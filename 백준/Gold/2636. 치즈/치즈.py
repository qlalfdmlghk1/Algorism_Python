from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

dr,dc = [1,-1,0,0],[0,0,1,-1]

visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n) :
    for j in range(m) : 
        if i == 0 or i == n-1 or j == 0 or j == m-1 :
            graph[i][j] = -1
            visited[i][j] = True

def bfs(r,c) :
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r,nex_c = cur_r + dr[i], cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < m and not visited[nex_r][nex_c] and graph[nex_r][nex_c] == 0 :
                graph[nex_r][nex_c] = -1
                visited[nex_r][nex_c] = True
                q.append((nex_r,nex_c))

def melting(melting_list,cur_r,cur_c) :
    # 1방향이라도 공기가 있으면 녹음
    for i in range(4) :
        nex_r = cur_r + dr[i]
        nex_c = cur_c + dc[i]
        if graph[nex_r][nex_c] == -1 :
            melting_list.append((cur_r,cur_c))
            return
    return

remain = 0
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == -1 :
            bfs(i,j)
        if graph[i][j] == 1 :
            remain += 1
    
cnt = 0
while remain :
    melting_list = []
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 :
                melting(melting_list,i,j)

    remain -= len(melting_list)
    if remain == 0 :
        last = len(melting_list)
    for ml in melting_list :
        a,b = ml
        graph[a][b] = -1
        bfs(a,b)
    cnt += 1

print(cnt)
print(last)