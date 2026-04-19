# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1
from collections import deque
n = int(input())
q = deque()
graph = [[] for _ in range(n+1)]
for _ in range(n) :
    nodes = list(map(int,input().split()))
    cnt_node = nodes[0]
    ind = 1
    while nodes[ind] != -1 :
        graph[cnt_node].append((nodes[ind],nodes[ind+1]))
        ind += 2

def bfs(v) :
    q.append((v,0))
    visited = [-1] * (n+1)
    visited[v] = True
    res = [0,0]
    while q :
        cur_node,cur_cost = q.popleft()
        for nex_node,nex_cost in graph[cur_node] :
            if visited[nex_node] == -1 :
                sum_cost = cur_cost + nex_cost
                q.append((nex_node,sum_cost))
                visited[nex_node] = True
                if res[1] < sum_cost :
                    res[1] = sum_cost
                    res[0] = nex_node
    return res

print(bfs(bfs(1)[0])[1])
