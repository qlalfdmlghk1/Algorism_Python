# import sys
# input = sys.stdin.readline
# from collections import deque
#
# cnt = 0   #상어가 먹은 물고기 수
# size = 2  #처음 상어 크기
#
# n = int(input())
# graph = []
# for _ in range(n) :
#     graph.append(list(map(int, input().split())))
#
# for i in range(n) :
#     for j in range(n) :
#         if graph[i][j] == 9 :
#             start_r, start_c = i,j
#
# q = deque()
# q.append((start_r,start_c)) #먹을 물고기 저장
#
# #현재 상어 size보다 작은 물고기들 q에 저장
# def set_fish(size) :
#     global q
#     for i in range(n) :
#         for j in range(n) :
#             if graph[i][j] != -1 and graph[i][j] != 0 and graph[i][j] < size :
#                 q.append((i,j))
#                 graph[i][j] = -1
#
# q3 = deque()
# # 물고기 먹을 때마다 거리 다시 계산
# def check_distance(r,c) :
#     global q3
#     while q :
#         cur_r,cur_c = q.popleft()
#         distance = (cur_r-r)**2 + (cur_c-c)**2
#         q3.append((distance, cur_r, cur_c))
#     q3 = sorted(q3)
#
#
# #현재 위치에서 다음 물고기까지 거리 계산
# def bfs(r,c,r2,c2) :
#     global cnt
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     dr = [-1, 0, 1, 0]
#     dc = [0, -1, 0, 1]
#     q2 = deque()
#     q2.append((r, c))
#     visited[r][c] = 0
#     while q2 :
#         cur_r, cur_c = q2.popleft()
#         for i in range(4) :
#             nex_r = cur_r + dr[i]
#             nex_c = cur_c + dc[i]
#             if 0 <= nex_r < n and 0 <= nex_c < n and not visited[nex_r][nex_c] and graph[nex_r][nex_c] <= size:
#                 if nex_r == r2 and nex_c == c2 :
#                     cnt += 1
#                     return visited[cur_r][cur_c] + 1
#                 visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
#                 q2.append((nex_r,nex_c))
#
#
# answer = 0
# idx = 1
# set_fish(size)  # q에 현재 size보다 작은 물고기들 위치 저장
# check_distance(start_r,start_c)  # q에 있는 물고기들 거리 짧은 순 정렬 -> q3에 저장
#
#
# while idx < len(q3) :
#     print(q3)
#     r,c = q3.popleft()
#     r2, c2 = q3.popleft()
#     answer += bfs(r,c,r2,c2)  # 다음 위치에 저장된다면
#     check_distance(r2, c2)    #
#     if cnt == size :          # 물고기 크기가 변경된다면
#         size += 1
#         cnt = 0
#         set_fish(size)        # 그 크기에 맞춰 다시 q 조정 -> q에 추가하고
#     idx += 1
#
# print(answer)

import sys
input = sys.stdin.readline
from collections import deque

# 상어가 먹은 물고기 수와 크기
cnt = 0
size = 2

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상어의 시작 위치를 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start_r, start_c = i, j
            graph[i][j] = 0  # 상어 위치를 빈칸으로 바꿈


# 상어가 먹을 수 있는 물고기 찾기 (거리와 위치 반환)
def bfs(shark_r, shark_c, shark_size):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    dist = [[-1] * n for _ in range(n)]
    dist[shark_r][shark_c] = 0

    q = deque([(shark_r, shark_c)])
    fish_list = []

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            nex_r, nex_c = cur_r + dr[i], cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < n and dist[nex_r][nex_c] == -1 and graph[nex_r][nex_c] <= shark_size:
                dist[nex_r][nex_c] = dist[cur_r][cur_c] + 1
                q.append((nex_r, nex_c))
                if 0 < graph[nex_r][nex_c] < shark_size:  # 먹을 수 있는 물고기
                    fish_list.append((dist[nex_r][nex_c], nex_r, nex_c))

    if not fish_list:    # 물고기가 없으면 return
        return
    fish_list.sort()     # 거리 -> 행 -> 열 순으로 정렬
    return fish_list[0]  # 가장 가까운 물고기 반환


answer = 0  # 총 이동 거리
while True:
    result = bfs(start_r, start_c, size)  # 먹을 물고기 찾기
    if result is None:  # 더 이상 먹을 물고기가 없으면 종료
        break

    distance, fish_r, fish_c = result
    answer += distance                 # 이동 거리 추가
    start_r, start_c = fish_r, fish_c  # 상어 위치 갱신
    graph[fish_r][fish_c] = 0          # 먹은 물고기 제거
    cnt += 1                           # 먹은 물고기 수 증가

    if cnt == size:  # 상어 크기 증가
        size += 1
        cnt = 0

print(answer)
