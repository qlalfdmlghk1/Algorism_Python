maze = [[1, 4], [0, 0], [2, 3]]
# result = 3
from collections import deque
q_red = deque()
q_blue = deque()
n = len(maze)
m = len(maze[0])
dr = [1,-1,0,0]
dc = [0,0,1,-1]

visited_red = [[1 for _ in range(m)]for _ in range(n)]
visited_blue = [[1 for _ in range(m)]for _ in range(n)]
def bfs(r_r,c_r, r_b,c_b) :
    res1,res2 = 0,0
    q_red.append((r_r,c_r))
    q_blue.append((r_b, c_b))
    while q_red or q_blue :
        print(q_red)
        print(q_blue)
        if q_red :
            cur_r_r,cur_c_r = q_red.popleft()
        if q_blue :
            cur_r_b,cur_c_b = q_blue.popleft()
        for i in range(4) :
            next_r_r = cur_r_r + dr[i]
            next_c_r = cur_c_r + dc[i]
            next_r_b = cur_r_b + dr[i]
            next_c_b = cur_c_b + dc[i]
            if (0 <= next_r_r < n and 0 <= next_c_r < m and visited_red[next_r_r][next_c_r] == 1
                    and (maze[next_r_r][next_c_r] == 0 or maze[next_r_r][next_c_r] == 3)) :
                if (next_r_r == r_r_end and next_c_r == r_c_end) :
                    res1 = visited_red[next_r_r][next_c_r]
                else :
                    q_red.append((next_r_r,next_c_r))
                    visited_red[next_r_r][next_c_r] = visited_red[cur_r_r][cur_c_r] + 1

            if (next_r_r != next_r_b or next_c_r != next_c_b) :
                if (0 <= next_r_b < n and 0 <= next_c_b < m and visited_blue[next_r_b][next_c_b] == 1
                    and (maze[next_r_b][next_c_b] == 0 or maze[next_r_b][next_c_b] == 4)) :
                    if (next_r_b == b_r_end and next_c_b == b_c_end) :
                        res2 = visited_blue[next_r_b][next_c_b]
                    else :
                        q_blue.append((next_r_b, next_c_b))
                        visited_blue[next_r_b][next_c_b] = visited_blue[cur_r_b][cur_c_b] + 1
    print(max(res1, res2))

for i in range(n) :
    for j in range(m) :
        if maze[i][j] == 1 :
            r_r_start = i
            r_c_start = j
        if maze[i][j] == 2 :
            b_r_start = i
            b_c_start = j
        if maze[i][j] == 3 :
            r_r_end = i
            r_c_end = j
        if maze[i][j] == 4 :
            b_r_end = i
            b_c_end = j


bfs(r_r_start,r_c_start,b_r_start,b_c_start)

