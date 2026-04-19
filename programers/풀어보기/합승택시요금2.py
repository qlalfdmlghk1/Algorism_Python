n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# result = 18
import heapq
graph = [[] for _ in range(n+1)]
for u,v,fare in fares :
    graph[u].append((fare, v))
    graph[v].append((fare, u))

answer = []
pq = []
list2 = [s,a,b]

cost_total = [0] * (n+1)
cost = [[214700000] * (n+1) for _ in range(3)]
cost[0][s] = 0
cost[1][a] = 0
cost[2][b] = 0

for i in range(3) :
    pq.append((0, list2[i]))
    while pq :
        cur_fare,cur_node = heapq.heappop(pq)
        for next_fare,next_node in graph[cur_node] :
            if cost[i][next_node] > cost[i][cur_node] :
                heapq.heappush(pq,(next_fare,next_node))
                cost[i][next_node] = next_fare + cost[i][cur_node]
    pq = []

for i in range(1,n+1) :
    cost_total[i] = cost[0][i] + cost[1][i] + cost[2][i]
print(min(cost_total[1:]))


