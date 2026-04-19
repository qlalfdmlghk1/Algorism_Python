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

prev = [0] * (N+1)

distance[start] = 0

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
            prev[nex_node] = cur_node

path = []
node = end
while node != start : 
    path.append(node)
    node = prev[node]
path.append(start)
path.reverse()

print(distance[end])
print(len(path))
print(*path)