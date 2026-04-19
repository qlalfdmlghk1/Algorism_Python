n, m = map(int, input().split())
friends = [[] for _ in range(n)]
answer = 0

for i in range(m):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)

visited = [False for _ in range(n)]


def dfs(depth, x):
    global answer
    if depth == 4:
        answer = 1
        return answer

    for i in friends[x]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False


for i in range(n):
    visited[i] = True
    result = dfs(0, i)
    if result == 1 :
      break

    visited[i] = False

print(answer)