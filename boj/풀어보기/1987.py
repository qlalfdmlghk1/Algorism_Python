# import sys
# input = sys.stdin.readline
# from collections import deque
# r,c = map(int,input().split())
# visited = [[1 for _ in range(c)] for _ in range(r)]
# q = deque()
# graph = []
#
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
# for i in range(r) :
#     graph.append(input())
#
# stack = []
# answer = 0
# cnt = 1
# def dfs(y,x) :
#     global cnt
#     global answer
#
#     for i in range(4) :
#         nr = y + dr[i]
#         nc = x + dc[i]
#         if 0 <= nr < r and 0<= nc < c and visited[nr][nc] == 1 and graph[nr][nc] not in stack :
#             visited[nr][nc] = visited[y][x] + 1
#             stack.append(graph[nr][nc])
#             cnt += 1
#             answer = max(answer, len(stack))
#             dfs(nr,nc)
#             visited[nr][nc] = 1
#             stack.pop()
#
# stack.append(graph[0][0])
# dfs(0,0)
# print(answer)

def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
            continue
        if visited[ord(alphaGrid[nx][ny]) - 65] == 0:
            visited[ord(alphaGrid[nx][ny]) - 65] = 1
            dfs(nx, ny, count+1)
            visited[ord(alphaGrid[nx][ny]) - 65] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
alphaGrid = []
for _ in range(r):
    alphaGrid.append(list(map(str, input())))

visited = [0] * 26
visited[ord(alphaGrid[0][0])-65] = 1

answer = 1

dfs(0, 0, 1)

print(answer)
