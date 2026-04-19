import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 방문 상태를 3차원 배열로 관리: visited[x][y][0 or 1] (벽 통과 여부)
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

# 방향 벡터
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# BFS 초기화
queue = deque([(0, 0, 0)])  # (row, col, wall_passed)
visited[0][0][0] = True

def bfs():
    steps = 0
    while queue:
        for _ in range(len(queue)):
            r, c, wall_passed = queue.popleft()

            # 도착 지점에 도달한 경우
            if r == n-1 and c == m-1:
                return steps + 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if graph[nr][nc] == 0 and not visited[nr][nc][wall_passed]:
                        visited[nr][nc][wall_passed] = True
                        queue.append((nr, nc, wall_passed))
                    elif graph[nr][nc] == 1 and wall_passed == 0 and not visited[nr][nc][1]:
                        visited[nr][nc][1] = True
                        queue.append((nr, nc, 1))
        steps += 1
    return -1

answer = bfs()
if answer != -1 :
    print(answer)
else :
    print(-1)


# sol1)
# import sys
# input = sys.stdin.readline
# from collections import deque
# n,m = map(int, input().split())
# graph = [[] for _ in range(n)]
# for i in range(n) :
#     k = input().strip()
#     for j in k :
#         graph[i].append(int(j))
#
# q = deque()
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# nr = [1,-1,0,0]
# nc = [0,0,1,-1]
# def bfs(r,c,w) :
#     visited[0][0] = 1
#     q.append((r,c,w))
#     while q:
#         cur_r, cur_c, cur_w = q.popleft()
#         if cur_r == n - 1 and cur_c == m - 1:
#             return visited[n-1][m-1]
#         for i in range(4):
#             nex_r = cur_r + nr[i]
#             nex_c = cur_c + nc[i]
#             if 0 <= nex_r < n and 0 <= nex_c < m and visited[nex_r][nex_c] == False :
#                 if graph[nex_r][nex_c] == 0 :
#                     visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
#                     q.append((nex_r, nex_c, 0))
#                 elif graph[nex_r][nex_c] == 1 and cur_w == 0:
#                     visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
#                     q.append((nex_r, nex_c, 1))
#     return -1
# print(bfs(0,0,0))


# sol2)
# import sys
# input = sys.stdin.readline
# from collections import deque
# n,m = map(int, input().split())
# graph = [[] for _ in range(n)]
# for i in range(n) :
#     k = input().strip()
#     for j in k :
#         graph[i].append(int(j))
#
# dic_wall = []
# for i in range(n) :
#     for j in range(m) :
#         if graph[i][j] == 1 :
#             dic_wall.append((i,j))
# dic_wall.append((0,0))
#
# nr = [1,-1,0,0]
# nc = [0,0,1,-1]
#
# answer = 214700000
#
# for wall in dic_wall :
#     y,x = wall[0], wall[1]
#     q = deque()
#     graph[y][x] = 0
#     visited = [[214700000 for _ in range(m)] for _ in range(n)]
#     visited[0][0] = 1
#     q.append((0,0))
#     while q:
#         cur_r, cur_c = q.popleft()
#         for i in range(4):
#             nex_r = cur_r + nr[i]
#             nex_c = cur_c + nc[i]
#             if 0 <= nex_r < n and 0 <= nex_c < m and visited[nex_r][nex_c] == 214700000 and graph[nex_r][nex_c] == 0:
#                 visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
#                 q.append((nex_r, nex_c))
#     answer = min(answer,visited[n-1][m-1])
#     graph[y][x] = 1
#
# if answer == 214700000 :
#     print(-1)
# else :
#     print(answer)