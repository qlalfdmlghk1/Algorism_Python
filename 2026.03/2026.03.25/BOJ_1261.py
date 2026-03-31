from collections import deque
M,N = map(int,input().split())
graph = []
for _ in range(N) :
    graph.append(list(map(int,input())))

INF = int(1e9)
distance = [[INF] * M for _ in range(N)]
distance[0][0] = 0

dr,dc = [1,-1,0,0],[0,0,1,-1]
q = deque([(0,0,0)])

while q :
    cur_distance,cur_r,cur_c = q.popleft()
    if cur_distance > distance[cur_r][cur_c] :
        continue
    for i in range(4) :
        nex_r = cur_r + dr[i]
        nex_c = cur_c + dc[i]
        if 0 <= nex_r < N and 0 <= nex_c < M :
            w = graph[nex_r][nex_c]
            if cur_distance + w < distance[nex_r][nex_c] :
                distance[nex_r][nex_c] = cur_distance + w
                if w == 0 :
                    q.appendleft((cur_distance, nex_r,nex_c))
                else :
                    q.appendleft((cur_distance + 1, nex_r,nex_c))
print(distance[N-1][M-1])