import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]  # [[], [2, 3, 4], [1, 5, 6], [1], [1, 7, 8], [2], [2], [4], [4]]
dp = [[0,0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1) :
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur) :
    global graph
    global visited
    visited[cur] = True
    if len(graph[cur]) == 0 :
        dp[cur][1] = 1
        dp[cur][0] = 0
    else :
        for nex in graph[cur] :  # 자신이 루트 노드인 서브트리를 조회
            if not visited[nex] :
                dfs(nex)
                dp[cur][1] += min(dp[nex][0], dp[nex][1])
                dp[cur][0] += dp[nex][1]
        dp[cur][1] += 1
dfs(1)
print(min(dp[1][0], dp[1][1]))