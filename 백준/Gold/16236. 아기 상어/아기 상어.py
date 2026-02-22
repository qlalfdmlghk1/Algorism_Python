import sys
input = sys.stdin.readline
from heapq import heapify,heappush
from collections import deque
N = int(input())
graph = []
for _ in range(N) :
    graph.append(list(map(int,input().split())))

dr,dc = [1,-1,0,0],[0,0,1,-1]

def bfs(start_r,start_c) :
    global size
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((start_r,start_c))
    visited[start_r][start_c] = 0
    candidate = []
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < N and 0 <= nex_c < N :
                if graph[nex_r][nex_c] <= size and visited[nex_r][nex_c] == -1 :
                    q.append((nex_r,nex_c))
                    visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
                    if 0 < graph[nex_r][nex_c] < size :
                        candidate.append((visited[nex_r][nex_c],nex_r,nex_c))
    if candidate :
        return min(candidate)
    else :
        return False

for i in range(N) :
        for j in range(N) :
            if graph[i][j] == 9 :
                shark_r,shark_c = i,j

time,cnt,size = 0,0,2

while True :
    target = bfs(shark_r,shark_c)

    if target :
        target_time,target_r,target_c = target
        graph[target_r][target_c] = 9
        graph[shark_r][shark_c] = 0
        shark_r,shark_c = target_r,target_c

        time += target_time
        cnt += 1
        
        if cnt == size :
            cnt = 0
            size += 1
    else :
        print(time)
        break
    