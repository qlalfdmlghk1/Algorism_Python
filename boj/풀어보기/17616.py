n, m, x = map(int, input().split())  # n: 노드 수, m: 간선 수, x: 특정 노드

up   = [[] for _ in range(n + 1)]
down = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    down[a].append(b)  # a 아래에 b가 있음
    up[b].append(a)    # b 위에 a가 있음

visited = [False] * (n + 1)

def dfs(x, graph):
    visited[x] = True
    count = 1              # 현재 노드를 포함한 카운트
    for nex in graph[x]:   # 현재 노드와 연결된 모든 노드에 대해
        if not visited[nex]:
            count += dfs(nex, graph)
    return count

visited = [False] * (n + 1)
up_count = dfs(x, up) - 1       # x를 기준으로 상위 노드 개수를 계산

visited = [False] * (n + 1)
down_count = dfs(x, down) - 1   # x를 기준으로 하위 노드 개수를 계산

print(1 + up_count, end=" ")
print(n - down_count)
