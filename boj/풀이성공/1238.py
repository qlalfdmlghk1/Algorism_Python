import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n,m,x = map(int,input().split())  # n명 학생, m개 도로, x번 도시 파티

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))

INF = int(1e9)

def dijkstra(start) :
    distance = [INF] * (n+1)
    pq = [(0,start)]
    distance[start] = 0
    while pq :
        cur_distance, cur_node = heappop(pq)
        if distance[cur_node] < cur_distance :
            continue

        for nex_distance, nex_node in graph[cur_node] :
            new_distance = cur_distance + nex_distance
            if new_distance < distance[nex_node] :
                distance[nex_node] = new_distance
                heappush(pq,(new_distance,nex_node))
    return distance

distance_from_x = dijkstra(x)
round_trip = [0] * (n+1)

for i in range(1,n+1) :
    distance_to_x = dijkstra(i)
    round_trip[i] = distance_to_x[x] + distance_from_x[i]

print(max(round_trip[1:]))