import sys
input = sys.stdin.readline
from heapq import heappop,heappush
t = int(input())
for _ in range(t) :
    n,d,c = map(int,input().split())  # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 개수

    graph = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)
    starts = []

    for _ in range(d) :
        a,b,s = map(int,input().split())  # a가 b를 의존 -> b가 감염되면 s초 후 a 감염
        graph[b].append((s,a))
        starts.append(b)

    def dijkstra(x) :
        pq = [(0,x)]
        distance[x] = 0

        while pq :
            cur_dist,cur_com = heappop(pq)

            if distance[cur_com] < cur_dist :
                continue

            for nex_distance,nex_com in graph[cur_com] :
                new_dist = cur_dist + nex_distance

                if new_dist < distance[nex_com] :
                    distance[nex_com] = new_dist
                    heappush(pq,(new_dist,nex_com))

    dijkstra(c)

    cnt = 0
    maxi = 0
    for d in distance[1:] :
        if d < 1e9 :
            cnt += 1
            maxi = max(maxi,d)
    print(cnt, maxi)
