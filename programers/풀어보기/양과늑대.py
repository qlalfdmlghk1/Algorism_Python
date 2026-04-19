from collections import deque
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

graph = [[] for _ in range(len(info) + 1)]
visited = [[-1, -1] for _ in range(len(info) + 1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque()
    q.append(start)
    visited[0] = [1, 0]
    while q:
        cur = q.popleft()
        for next_v in graph[cur]:
            if visited[next_v][1] == -1 :
                if info[next_v] == 0 :
                    visited[next_v][0] = visited[cur][0] + 1
                    visited[next_v][1] = visited[cur][1]
                    q.append(next_v)
                else :
                    visited[next_v][0] = visited[cur][0]
                    visited[next_v][1] = visited[cur][1] + 1
                    if visited[next_v][0] > visited[next_v][1]:
                        q.append(next_v)
                    else :
                        visited[next_v] = [-1,-1]


bfs(0)

print(visited)