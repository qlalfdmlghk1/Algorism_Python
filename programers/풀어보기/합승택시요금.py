n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# result = 82
import heapq
graph = [[] for _ in range(n+1)]
for u,v,fare in fares :
    graph[u].append((fare, v))
    graph[v].append((fare, u))

answer = []

pq_s = [(0,s)]
pq_a = [(0,a)]
pq_b = [(0,b)]
cost = [0] * (n+1)
cost_from_a = [-1] * (n+1)
cost_from_b = [-1] * (n+1)
cost_from_s = [-1] * (n+1)
cost_from_a[a] = 0
cost_from_b[b] = 0
cost_from_s[s] = 0

while pq_s :
    cur_fare,cur_node = heapq.heappop(pq_s)
    for next_fare,next_node in graph[cur_node] :
        if cost_from_s[next_node] == -1 :
            heapq.heappush(pq_s,(next_fare,next_node))
            cost_from_s[next_node] = next_fare + cost_from_s[cur_node]

while pq_a :
    cur_fare,cur_node = heapq.heappop(pq_a)
    for next_fare,next_node in graph[cur_node] :
        if cost_from_a[next_node] == -1 :
            heapq.heappush(pq_a,(next_fare,next_node))
            cost_from_a[next_node] = next_fare + cost_from_a[cur_node]

while pq_b :
    cur_fare,cur_node = heapq.heappop(pq_b)
    for next_fare,next_node in graph[cur_node] :
        if cost_from_b[next_node] == -1 :
            heapq.heappush(pq_b,(next_fare,next_node))
            cost_from_b[next_node] = next_fare + cost_from_b[cur_node]

for i in range(1,n+1) :
    cost[i] = cost_from_a[i] + cost_from_b[i] + cost_from_s[i]


for i in cost :
    if i > 0 :
        answer.append(i)
print(min(answer))

