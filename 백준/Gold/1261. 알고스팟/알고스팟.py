from heapq import heappush,heappop
M,N = map(int,input().split())
graph = []
for _ in range(N) :
    graph.append(list(map(int,input())))

INF = int(1e9)
distance = [[INF] * M for _ in range(N)]
distance[0][0] = 0

dr,dc = [1,-1,0,0],[0,0,1,-1]
pq = [(0,0,0)]

while pq :
    cur_distance,cur_r,cur_c = heappop(pq)
    for i in range(4) :
        nex_r = cur_r + dr[i]
        nex_c = cur_c + dc[i]
        if 0 <= nex_r < N and 0 <= nex_c < M :
            if distance[cur_r][cur_c] < cur_distance : 
                continue
            else :
                if graph[nex_r][nex_c] == 1 :
                    new_distance = distance[cur_r][cur_c] + 1
                else : 
                    new_distance = distance[cur_r][cur_c]
                if new_distance < distance[nex_r][nex_c] :
                    distance[nex_r][nex_c] = new_distance
                    heappush(pq,(new_distance,nex_r,nex_c))
print(distance[N-1][M-1])