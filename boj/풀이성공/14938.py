from heapq import heapify,heappush, heappop
n,m,r = map(int,input().split())  # 지역 수, 수색범위, 길의 개수
places = list(map(int,input().split()))
places.insert(0,0)

INF = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(r) :
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))

def dijkstra(start) :
    pq = [(0,start)]
    distance[start] = 0
    while pq :
        cur_dist,cur_node = heappop(pq)
        if distance[cur_node] < cur_dist :
            continue

        for nex_dist,nex_node in graph[cur_node] :
            new_dist = cur_dist + nex_dist
            if new_dist < distance[nex_node] :
                distance[nex_node] = new_dist
                heappush(pq, (new_dist, nex_node))

answer = 0
for i in range(1,n+1) :
    result = 0
    distance = [INF] * (n+1)
    dijkstra(i)
    for index,d in enumerate(distance) :
        if d <= m :
            result += places[index]
    answer = max(answer,result)
print(answer)