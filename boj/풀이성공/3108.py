from collections import deque
n = int(input())

board = [[0 for _ in range(2001)] for _ in range(2001)]
for _ in range(n) :
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500; x2 += 500; y1 += 500; y2 += 500
    x1 *= 2; x2 *= 2; y1 *= 2; y2 *= 2
    for i in range(y1,y2+1) :
        for j in range(x1,x2+1) :
            if i == y1 or i == y2:
                board[i][j] = 1
            if j == x1 or j == x2 :
                board[i][j] = 1

q = deque()
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs(r,c) :
    q.append((r,c))
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r <= 2000 and 0 <= nex_c <= 2000 and board[nex_r][nex_c] == 1 :
                board[nex_r][nex_c] = 0
                q.append((nex_r,nex_c))

cnt = 0
if board[1000][1000] == 1 :
    cnt -= 1
for i in range(2000) :
    for j in range(2000):
        if board[i][j] == 1 :
            bfs(i,j)
            cnt += 1

print(cnt)