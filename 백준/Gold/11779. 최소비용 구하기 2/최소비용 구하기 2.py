from heapq import heappush,heappop
N = int(input())
M = int(input())

INF = int(1e9)
distance = [INF for _ in range(N+1)]

graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

start,end = map(int,input().split())

route = [[] for _ in range(N+1)]

distance[start] = 0
route[start] = [start]

pq = [(0,start)]
while pq :
    cur_cost,cur_node = heappop(pq)

    if distance[cur_node] < cur_cost :
        continue

    for nex_cost,nex_node in graph[cur_node] :
        new_cost = distance[cur_node] + nex_cost
        if new_cost < distance[nex_node] :
            distance[nex_node] = new_cost
            heappush(pq,(new_cost,nex_node))
            route[nex_node] = route[cur_node] + [nex_node]

print(distance[end])
print(len(route[end]))
print(*route[end])