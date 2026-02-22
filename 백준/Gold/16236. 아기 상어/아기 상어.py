import sys
input = sys.stdin.readline
from heapq import heapify,heappush
from collections import deque
N = int(input())
graph = []
for _ in range(N) :
    graph.append(list(map(int,input().split())))

dr,dc = [1,-1,0,0],[0,0,1,-1]

def bfs(start_r,start_c, target_r, target_c) :
    global size
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((start_r,start_c))
    visited[start_r][start_c] = 0
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < N and 0 <= nex_c < N :
                if graph[nex_r][nex_c] <= size and visited[nex_r][nex_c] == -1 :
                    q.append((nex_r,nex_c))
                    visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
                if nex_r == target_r and nex_c == target_c :
                    return visited[nex_r][nex_c]
    return False

for i in range(N) :
        for j in range(N) :
            if graph[i][j] == 9 :
                shark_r,shark_c = i,j

time,cnt,size = 0,0,2

while True :
    pq = []
    heapify(pq)
    for i in range(N) :
        for j in range(N) :
            if size > graph[i][j] and graph[i][j] != 0 :
                distance = bfs(shark_r,shark_c,i,j)
                if distance :
                    heappush(pq,(distance, i,j))
    if pq :
        target_time,target_r,target_c = pq[0]
        graph[target_r][target_c] = 9
        graph[shark_r][shark_c] = 0
        shark_r,shark_c = target_r,target_c

        time += target_time
        cnt += 1
        
        if cnt >= size :
            cnt -= size
            size += 1
    else :
        print(time)
        break
