board = [".D.R", "....", ".G..", "...D"]  # R 시작, G 종료

from collections import deque
def solution(board):
    start_r = 0
    start_c = 0
    R,C = len(board), len(board[0])
    visited = [[False] * C for _ in range(R)]

    for i in range(R) :
        for j in range(C) :
            if board[i][j] == "R" :
                start_r,start_c = i,j

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    q = deque()
    q.append((start_r, start_c, 0))
    visited[start_r][start_c] = True


    while q :
        cur_r, cur_c, cur_cnt = q.popleft()

        if board[cur_r][cur_c] == "G" :  # 목표 지점 도달
            return cur_cnt

        for i in range(4) :
            nex_r,nex_c = cur_r, cur_c

            while True:  # 리코쳇 방식으로 끝까지 이동
                dis_r = nex_r + dr[i]
                dis_c = nex_c + dc[i]
                if 0 <= dis_r < R and 0 <= dis_c < C and board[dis_r][dis_c] != "D" :
                    nex_r,nex_c = dis_r,dis_c

                else :    # 벽이나 장애물에 닿으면, 멈춤 (while문 빠지기)
                    break

            if not visited[nex_r][nex_c] :
                nex_cnt = cur_cnt + 1
                q.append((nex_r,nex_c,nex_cnt))
                visited[nex_r][nex_c] = True    # 장애물이나 벽에 부딪히기 직전 칸 : visited = True
    return -1
print(solution(board))
