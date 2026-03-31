from heapq import heappush,heappop
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

start,end = map(int,input().split())

INF = int(1e9)
distance = [INF for _ in range(N+1)]
route = [[] for _ in range(N+1)]

pq = [(0,start)]
distance[start] = 0
route[start] = [start]

while pq :
    cur_distance, cur_node = heappop(pq)

    if distance[cur_node] < cur_distance :
        continue

    for nex_cost,nex_node in graph[cur_node] : 
        new_cost = distance[cur_node] + nex_cost
        if new_cost < distance[nex_node] :
            distance[nex_node] = new_cost
            route[nex_node] = route[cur_node] + [nex_node]
            heappush(pq,(new_cost,nex_node))


print(distance[end])
print(len(route[end]))
print(*route[end])