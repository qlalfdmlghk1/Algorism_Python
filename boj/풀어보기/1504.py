import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e) :
    arr = list(map(int,input().split()))
    graph[arr[0]].append((arr[2],arr[1]))
    graph[arr[1]].append((arr[2], arr[0]))
stop1, stop2 = map(int, input().split())

def dikstra(start,end) :
    pq = []
    result = 0xffffff
    pq = [(0,start)]
    distance = [0xffffff] * (n+1)
    distance[start] = 0
    while pq :
        cur_distance,cur_node = heappop(pq)
        # 해당 노드에 이미 더 짧은 길이로 방문했으면 PASS -> 그렇게 갈 필요가 없다.
        if distance[cur_node] < cur_distance :
            continue

        # 해당 노드에 지금 도달한 방법이 가장 짧은 거리일 경우
        for next_distance, next_node in graph[cur_node] :
            sum_distance = next_distance + cur_distance

            # 다음 방문할 노드의 거리가 현재 노드에서 새로운 경로의 거리를 더한 것보다 작다면
            if distance[next_node] > sum_distance :
                distance[next_node] = sum_distance
                heappush(pq,(sum_distance,next_node))
    return distance[end]


route1 = (dikstra(1,stop1) + dikstra(stop1,stop2) + dikstra(stop2,n))
route2 = (dikstra(1,stop2) + dikstra(stop2,stop1) + dikstra(stop1,n))
if route1 >= 0xffffff or route2 >= 0xffffff :
    print(-1)
else :
    print(min(route1,route2))