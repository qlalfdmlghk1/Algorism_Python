from collections import deque
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]
row = len(maps)
col = len(maps[0])
visited = [[-1 for _ in range(col)] for _ in range(row)]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited[r][c] = 1
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col:
                if visited[next_r][next_c] == -1 and maps[next_r][next_c] == 1:
                    visited[next_r][next_c] = visited[cur_r][cur_c] + 1
                    q.append((next_r, next_c))

bfs(0,0)
print(visited)
print(visited[row-1][col-1])