from collections import deque
from itertools import combinations

n,m = map(int,input().split()) # n : 연구소 크기, m : 바이러스 개수
grid = []
for i in range(n) :
    grid.append(input().split())
virus = []
answer = []
maxi = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == '2':
            virus.append((i, j))

for i in combinations(virus,m) :
    visited = [[0] * n for _ in range(n)]
    q = deque(i)
    virus_rest = list(set(virus) - set(q))
    # print(virus_rest)
    # print(virus_rest[0])
    # print(virus_rest[1])
    # print(virus_rest[0][0],virus_rest[0][1])
    for s in range(len(virus_rest)) :
        grid[virus_rest[s][0]][virus_rest[s][1]] = '*'
        visited[virus_rest[s][0]][virus_rest[s][1]] = -1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        cur_r, cur_c = q.popleft()
        for j in range(4):
            next_r = cur_r + dr[j]
            next_c = cur_c + dc[j]
            if 0 <= next_r < n and 0 <= next_c < n:
                if grid[next_r][next_c] == '0' and visited[next_r][next_c] == 0:
                    visited[next_r][next_c] = visited[cur_r][cur_c] + 1
                    q.append((next_r, next_c))
                # if grid[next_r][next_c] == '*' and visited[next_r][next_c] == 0:
                #     visited[next_r][next_c] = visited[cur_r][cur_c] + 1
                #     q.appendleft((next_r, next_c))

    for a in visited :
        for b in a :
            maxi = max(b,maxi)
    answer.append(maxi)
    # print(visited)
    # print(answer)

print(min(answer))