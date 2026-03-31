from heapq import heappush, heappop

N, M, A, B, C = map(int, input().split())

# 다익스트라
INF = int(1e9)
graph = [[] for _ in range(N + 1)]
costs = set()

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))
    costs.add(w)

def dijkstra(limit):
    dist = [INF] * (N + 1)
    dist[A] = 0
    pq = [(0, A)]

    while pq:
        cur_dist, cur_node = heappop(pq)

        if cur_dist > dist[cur_node]:
            continue

        for nex_cost, nex_node in graph[cur_node]:
            if nex_cost > limit:
                continue
            new_dist = cur_dist + nex_cost
            if new_dist < dist[nex_node]:
                dist[nex_node] = new_dist
                heappush(pq, (new_dist, nex_node))

    return dist[B]

costs = sorted(costs)
ans = -1

# 이분 탐색
low, high = 0, len(costs) - 1
while low <= high:
    mid = (low + high) // 2
    if dijkstra(costs[mid]) <= C:
        ans = costs[mid]
        high = mid - 1
    else:
        low = mid + 1

print(ans)
