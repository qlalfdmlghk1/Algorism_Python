rows,columns,queries = 100,97,[[1,1,100,97]]

from collections import deque
def solution(rows, columns, queries):
    answer = []
    # 1사분면에 놓고 반시계로 돌릴거임
    board = [[] for _ in range(rows)]
    for i in range(rows) :
        for j in range(1,columns+1) :
            board[i].append(i*columns + j)

    for querie in queries :
        x1,y1,x2,y2 = querie[0]-1,querie[1]-1,querie[2]-1,querie[3]-1
        rotate_list = deque()
        for i in range(y1,y2+1) :  # 맨 아래 행
            rotate_list.append(board[x1][i])
        for i in range(x1+1,x2+1) :  # 맨 오른쪽 열
            rotate_list.append(board[i][y2])
        for i in range(y2-1,y1-1,-1) :  # 맨 윗 행
            rotate_list.append(board[x2][i])
        for i in range(x2-1,x1,-1) :  # 맨 왼쪽 열
            rotate_list.append(board[i][y1])
        # print("rotate_list",rotate_list)

        answer.append(min(rotate_list))

        rotate_list.appendleft(rotate_list.pop())

        for i in range(y1,y2+1) :  # 맨 아래 행
            board[x1][i] = rotate_list.popleft()
        for i in range(x1+1,x2+1) :  # 맨 오른쪽 열
            board[i][y2] = rotate_list.popleft()
        for i in range(y2-1,y1-1,-1) :  # 맨 윗 행
            board[x2][i] = rotate_list.popleft()
        for i in range(x2-1,x1,-1) :  # 맨 왼쪽 열
            board[i][y1] = rotate_list.popleft()

    return answer

print(solution(rows,columns,queries))