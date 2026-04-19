import sys
input = sys.stdin.readline
from heapq import heappush,heappop
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    u,v,cost = map(int,input().split())
    graph[u].append((cost,v))
    # graph[v].append((cost,u))
s,e = map(int,input().split())

def dikstra(start,end) :
    pq = []
    costs = [214700000] * (n+1)
    pq.append((0,start))
    costs[start] = 0
    while pq :
        cur_cost, cur_node = heappop(pq)
        if costs[cur_node] < cur_cost :
            continue
        for next_costs, next_node in graph[cur_node] :
            sum_costs = cur_cost + next_costs
            if costs[next_node] > sum_costs :
                costs[next_node] = sum_costs
                heappush(pq,(sum_costs,next_node))
    return costs[end]

print(dikstra(s,e))