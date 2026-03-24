import sys
input = sys.stdin.readline
from heapq import heappush, heappop
cnt = 0
while True :
    N = int(input())

    if N == 0 :
        break

    graph = []
    for _ in range(N) :
        graph.append(list(map(int,input().split())))

    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = graph[0][0]
    
    dr,dc = [1,-1,0,0],[0,0,1,-1]
    
    pq = [(distance[0][0],0,0)]
    while pq :
        cur_cost, cur_r, cur_c = heappop(pq)
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < N and 0 <= nex_c < N :
                new_cost = cur_cost + graph[nex_r][nex_c]
                if cur_cost > distance[cur_r][cur_c] :
                    continue
                else :
                    if new_cost < distance[nex_r][nex_c]  :
                        distance[nex_r][nex_c] = new_cost
                        heappush(pq,(new_cost,nex_r,nex_c))
    cnt += 1 
    print("Problem " + str(cnt) + ": " + str(distance[N-1][N-1]))      