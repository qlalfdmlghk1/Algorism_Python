from collections import deque
import copy
import sys
input = sys.stdin.readline

r,c,T = map(int, input().split())
grid = []

for _ in range(r) :
    grid.append(list(map(int,input().split())))

air_cleaner = []

for i in range(r) :
    if grid[i][0] == -1 :
        air_cleaner.append(i)
    if len(air_cleaner) == 2 :
        break

upper_air_cleaner = air_cleaner[0]
lower_air_cleaner = air_cleaner[1]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dust(cur_r,cur_c) :
    global new_grid
    spread = grid[cur_r][cur_c] // 5
    cnt = 0
    for i in range(4) :
        nex_r, nex_c = cur_r + dr[i], cur_c + dc[i]
        if 0 <= nex_r < r and 0 <= nex_c < c and grid[nex_r][nex_c] != -1 :
            new_grid[nex_r][nex_c] += spread
            cnt += 1
    new_grid[cur_r][cur_c] += grid[cur_r][cur_c] - (spread * cnt)


def air_clean() :
    global grid
    global air_cleaner
    q1 = deque()
    q1.append(0)
    for j in range(1, c):
        q1.append(grid[upper_air_cleaner][j])
    for i in range(upper_air_cleaner-1, -1, -1):
        q1.append(grid[i][c-1])
    for j in range(c-2, -1, -1):
        q1.append(grid[0][j])
    for i in range(1, upper_air_cleaner-1):
        q1.append(grid[i][0])
    # print(q1)

    for j in range(1, c):
        grid[upper_air_cleaner][j] = q1.popleft()
    for i in range(upper_air_cleaner-1,-1,-1):
        grid[i][c-1] = q1.popleft()
    for j in range(c-2,-1,-1):
        grid[0][j] = q1.popleft()
    for i in range(1, upper_air_cleaner):
        grid[i][0] = q1.popleft()

    q2 = deque()
    q2.append(0)
    for j in range(1,c) :
        q2.append(grid[lower_air_cleaner][j])
    for i in range(lower_air_cleaner+1,r) :
        q2.append(grid[i][c-1])
    for j in range(c-2,-1,-1) :
        q2.append(grid[r-1][j])
    for i in range(r-2,lower_air_cleaner+1,-1) :
        q2.append(grid[i][0])
    # print(q2)

    for j in range(1,c) :
        grid[lower_air_cleaner][j] = q2.popleft()
    for i in range(lower_air_cleaner+1,r) :
        grid[i][c-1] = q2.popleft()
    for j in range(c-2,-1,-1) :
        grid[r-1][j] = q2.popleft()
    for i in range(r-2,lower_air_cleaner,-1) :
        grid[i][0] = q2.popleft()


for t in range(T) :
    new_grid = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if grid[i][j] > 0 :
                dust(i,j)
    grid = copy.deepcopy(new_grid)
    air_clean()
    grid[upper_air_cleaner][0] = -1
    grid[lower_air_cleaner][0] = -1

# print(grid)
answer = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] > 0:  # 공기청정기(-1) 제외
            answer += grid[i][j]
print(answer)
