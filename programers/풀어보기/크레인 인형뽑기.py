board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = 0
stack = []
board.append([-1] * len(board[0]))

while moves:
    for i in range(len(board)):
        if board[i][moves[0] - 1] == -1:
            moves.pop(0)

        elif board[i][moves[0] - 1] != 0:
            if not stack:
                stack.append(board[i][moves[0] - 1])
                board[i][moves[0] - 1] = 0
                moves.pop(0)
                break
            elif stack[-1] == board[i][moves[0] - 1]:
                answer += 2
                stack.pop()
                board[i][moves[0] - 1] = 0
                moves.pop(0)
                break
            else:
                stack.append(board[i][moves[0] - 1])
                board[i][moves[0] - 1] = 0
                moves.pop(0)
                break

print(answer)