from collections import deque
from itertools import combinations
n,m = map(int,input().split())
grid = []
for i in range(n) :
    grid.append(input().split())
row_len = len(grid)
col_len = len(grid[0])
wall = []
answer = []
#print(grid)


for i in range(row_len) :
    for j in range(col_len):
        if grid[i][j] == '0' :
            wall.append([i,j])

def bfs(x, y):
    cnt = 0
    #visited = [[False] * col_len for _ in range(row_len)]
    q = deque()
    q.append((x, y))

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row_len and 0 <= next_c < col_len:
                if visited[next_r][next_c] == False and grid[next_r][next_c] == '0':
                    visited[next_r][next_c] = True
                    q.append((next_r, next_c))





for i in combinations(wall,3) :
    visited = [[False] * col_len for _ in range(row_len)]
    grid[i[0][0]][i[0][1]] = '1'
    grid[i[1][0]][i[1][1]] = '1'
    grid[i[2][0]][i[2][1]] = '1'

    cnt = 0

    for j in range(row_len) :
        for k in range(col_len) :
            if grid[j][k] == '2' :
                bfs(j,k)

    for a in range(row_len):
        for b in range(col_len):
            if grid[a][b] == '2' or grid[a][b] == '1' :
                visited[a][b] = True
            if visited[a][b] == False :
                cnt += 1
    answer.append(cnt)


    grid[i[0][0]][i[0][1]] = '0'
    grid[i[1][0]][i[1][1]] = '0'
    grid[i[2][0]][i[2][1]] = '0'

#print(answer)
print(max(answer))
