from collections import deque
# 동 서 남 북 상 하  순서
dr = [0,0,1,-1,0,0]  
dc = [1,-1,0,0,0,0]
dl = [0,0,0,0,1,-1]

def bfs(start_r, start_c, start_l, end_r, end_c, end_l) :
    q = deque()
    q.append((start_l,start_r,start_c))
    visited[start_l][start_r][start_c] = 0
    while q :
        cur_l,cur_r,cur_c = q.popleft()
        for i in range(6) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            nex_l = cur_l + dl[i]
            if 0 <= nex_r < R and 0 <= nex_c < C and 0 <= nex_l < L :
                if graph[nex_l][nex_r][nex_c] != "#" and not visited[nex_l][nex_r][nex_c] :
                    q.append((nex_l,nex_r,nex_c))
                    visited[nex_l][nex_r][nex_c] = visited[cur_l][cur_r][cur_c] + 1
                    if nex_l == end_l and nex_r == end_r and nex_c == end_c :
                        return visited[nex_l][nex_r][nex_c]
    return False

while True :
    L,R,C = map(int,input().split()) # 충 수, 행 수, 열 수
    if L == 0 and R == 0 and C == 0 :
        break
    graph = []
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for i in range(L) :
        floor = []
        for _ in range(R+1) :
            floor.append(list(input()))    
        floor.pop()
        graph.append(floor)
    
    for i in range(L) : 
        for j in range(R) : 
            for k in range(C) :
                if graph[i][j][k] == "S" :
                    start_l,start_r,start_c = i,j,k
                if graph[i][j][k] == "E" :
                    end_l,end_r,end_c = i,j,k

    answer = bfs(start_r, start_c, start_l, end_r, end_c, end_l)
    if answer :
        print("Escaped in",answer, "minute(s).")
    else :
        print("Trapped!")