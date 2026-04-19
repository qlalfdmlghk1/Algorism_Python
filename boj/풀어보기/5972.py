from heapq import heappush,heappop
n,m = map(int,input().split())  # 헛간 수, 길의 수
MAX = int(1e9)
distance = [MAX] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))

def dijkstra(start) :
    pq = [(0,start)]
    distance[start] = 0
    while pq :
        cur_distance, cur_node = heappop(pq)
        if distance[cur_node] < cur_distance :
            continue

        for nex_distance, nex_node in graph[cur_node] :
            new_distance = nex_distance + cur_distance
            if new_distance < distance[nex_node] :
                distance[nex_node] = new_distance
                heappush(pq,(new_distance,nex_node))

dijkstra(1)

print(distance[n])