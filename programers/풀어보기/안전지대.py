board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
len_r = len(board)
len_c = len(board[0])
dr = [0,0,1,-1,1,-1,1,-1]
dc = [1,-1,0,0,1,-1,-1,1]
answer = 0

def check(r,c) :
    cnt = 1
    for i in range(8) :
        nr = dr[i] + r
        nc = dc[i] + c
        if 0 <= nr < len_r and 0 <= nc < len_c and board[nr][nc] == 0 :
            cnt += 1
            board[nr][nc] = 2
    return cnt


for i in range(len_r) :
    for j in range(len_c):
        if board[i][j] == 1 :
            answer += check(i,j)

print(len_r * len_c - answer)