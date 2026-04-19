import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
graph = []
for _ in range(N) :
    graph.append(list(map(int,input().split())))

dr,dc = [1,-1,0,0], [0,0,1,-1]
def dfs(r,c,depth,total) :
    global answer
    if depth == 4 :
        answer = max(answer,total)
        return
    
    # 가지치기
    if total + max_val * (4-depth) <= answer :
        return
    for i in range(4) :
        nex_r,nex_c = r + dr[i], c + dc[i]
        if 0 <= nex_r < N and 0 <= nex_c < M and not visited[nex_r][nex_c] :
            visited[nex_r][nex_c] = True
            dfs(nex_r,nex_c,depth+1,total+graph[nex_r][nex_c])
            visited[nex_r][nex_c] = False

def check_shape(r,c) :
    global answer 
    arms = []
    for i in range(4) :
        nex_r,nex_c = r + dr[i], c + dc[i]
        if 0 <= nex_r < N and 0 <= nex_c < M :
            arms.append(graph[nex_r][nex_c])
        
    # 팔이 3개 이상이어야 T자 가능
    if len(arms) >= 3 :
        if len(arms) == 4 :
            answer = max(answer,graph[r][c] + sum(arms) - min(arms))
        else :
            answer = max(answer,graph[r][c] + sum(arms))

answer = 0
visited = [[False for _ in range(M)] for _ in range(N)]
max_val = max(max(row) for row in graph)
for i in range(N) :
    for j in range(M) :
        visited[i][j] = True
        dfs(i,j,1, graph[i][j])
        visited[i][j] = False
        check_shape(i,j)
print(answer)