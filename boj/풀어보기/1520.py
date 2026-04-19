import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

m, n = map(int, input().split())
graph = []
visited = [[False for _ in range(n)] for _ in range(m)]

for _ in range(m):
    graph.append(list(map(int, input().split())))

# cnt = 0
# def dfs(cur_r,cur_c) :
#     global cnt
#     dr = [1,0,-1,0]
#     dc = [0,1,0,-1]
#     cur = graph[cur_r][cur_c]
#     for i in range(4) :
#         nex_r = cur_r + dr[i]
#         nex_c = cur_c + dc[i]
#         if 0 <= nex_r < m and 0 <= nex_c < n :
#             nex = graph[nex_r][nex_c]
#             # print(nex)
#             if not visited[nex_r][nex_c] and nex < cur :
#                 # print(nex_r,nex_c)
#                 if nex_r == m-1 and nex_c == n-1 :
#                     cnt += 1
#                 visited[nex_r][nex_c] = True
#                 dfs(nex_r,nex_c)
#                 visited[nex_r][nex_c] = False
#     return cnt
#
# print(dfs(0,0))

dp = [[-1 for _ in range(n)] for _ in range(m)]

# 이동 방향 (상, 하, 좌, 우)
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    # 도착 지점에 도달하면 1을 반환 (경로를 하나 찾은 것)
    if r == m - 1 and c == n - 1:
        return 1

    # 이미 방문한 적이 있으면 그 값을 반환
    if dp[r][c] != -1:
        return dp[r][c]

    # 현재 위치에서 갈 수 있는 경로 수
    dp[r][c] = 0

    for i in range(4):
        nex_r = r + dr[i]
        nex_c = c + dc[i]

        # 범위 내에 있고, 다음 이동할 곳이 현재보다 값이 작을 때만 이동
        if 0 <= nex_r < m and 0 <= nex_c < n:
            if graph[nex_r][nex_c] < graph[r][c]:
                dp[r][c] += dfs(nex_r, nex_c)

    return dp[r][c]

# (0,0)에서 출발
print(dfs(0, 0))










# def bfs(r,c) :
#     cnt = 0
#     q = deque()
#     q.append((r,c))
#     visited[r][c] = True
#     dr = [1, 0, -1, 0]
#     dc = [0,1,0,-1]
#     while q :
#         cur_r,cur_c = q.popleft()
#         cur = graph[cur_r][cur_c]
#         for i in range(4):
#             nex_r = cur_r + dr[i]
#             nex_c = cur_c + dc[i]
#             if 0 <= nex_r < m and 0 <= nex_c < n :
#                 nex = graph[nex_r][nex_c]
#                 # print(nex)
#                 if not visited[nex_r][nex_c] and nex < cur :
#                     # print(nex_r,nex_c)
#                     if nex_r == m-1 and nex_c == n-1 :
#                         cnt += 1
#     return cnt



# print(bfs(0,0))