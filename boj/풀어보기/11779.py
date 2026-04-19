from heapq import heappop, heappush

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s,d,r = map(int,input().split())
    graph[s].append((r,d))

start,destination = map(int,input().split())

distance = [1e9] * (n+1)
prev_node = [0] * (n+1)

def dikstra(start) :
    pq = []
    pq.append((0,start))
    while pq :
        cur_distance, cur_node = heappop(pq)
        if distance[cur_node] < cur_distance :
            continue
        for next_distance, next_node in graph[cur_node] :
            sum_distance = cur_distance + next_distance
            if distance[next_node] > sum_distance :
                distance[next_node] = sum_distance
                prev_node[next_node] = cur_node
                heappush(pq,(sum_distance,next_node))

distance[start] = 0
dikstra(start)
print(distance[destination])

now = destination
path = [destination]
while now != start :
    now = prev_node[now]
    path.append(now)
path.reverse()

print(len(path))
print(' '.join(map(str, path)))