from collections import deque
import heapq

cnt = 0
while True :    
    N = int(input())

    if N == 0 :
        break

    INF = int(1e9)
    graph = []
    
    for _ in range(N) :
        graph.append(list(map(int,input().split())))
    
    dr,dc = [1,-1,0,0],[0,0,1,-1]

    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = graph[0][0]
    pq = [(graph[0][0],0,0)]

    while pq :
        cur_cost,cur_r,cur_c = heapq.heappop(pq)
        if cur_cost > dist[cur_r][cur_c] :
            continue
        for i in range(4) :
            nex_r,nex_c = cur_r + dr[i], cur_c + dc[i]
            if 0 <= nex_r < N and 0 <= nex_c < N :
                new_cost = cur_cost + graph[nex_r][nex_c]
                if new_cost < dist[nex_r][nex_c] :
                    dist[nex_r][nex_c] = new_cost
                    heapq.heappush(pq,(new_cost,nex_r,nex_c))
    cnt += 1
    print("Problem " + str(cnt) + ":" + " " + str(dist[N-1][N-1]))
    