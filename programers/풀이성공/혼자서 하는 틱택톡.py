board = ["...", "...", "..."]

def solution(board):
    answer = 1
    player1,player2 = 0,0

    def is_player1_bingo() :
        # 빙고 가능 총 8가지 경우 확인
        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" :
            return True
        if board[1][0] == "O" and board[1][1] == "O" and board[1][2]  == "O" :
            return True
        if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
            return True
        if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
           return True
        if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
            return True
        if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            return True
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
           return True
        if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
           return True

    def is_player2_bingo() :
        # 빙고 가능 총 8가지 경우 확인
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" :
            return True
        if board[1][0] == "X" and board[1][1] == "X" and board[1][2]  == "X" :
            return True
        if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            return True
        if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
           return True
        if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            return True
        if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            return True
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
           return True
        if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
           return True

    # 안되는 경우
    # 1. X의 개수가 O보다 많을 때
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == "O" :
                player1 += 1
            elif board[i][j] == "X" :
                player2 += 1
    if player1 < player2 :
        return 0

    # 2. O의 개수가 X보다 2개 이상 많을 때
    if player1 > player2 + 1 :
        return 0

    # 3. 게임이 종료됐는데, 추가적인 동작이 있을 때
    if player1 >= 3 :
        if is_player1_bingo() and player1 == player2 :
            return 0
        if is_player2_bingo() and player1 > player2 :
            return 0

    return answer

print(solution(board))
