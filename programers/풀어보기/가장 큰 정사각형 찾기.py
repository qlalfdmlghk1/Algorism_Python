board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

def solution(board):
    n,m = len(board), len(board[0])
    dp = [[] for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            dp[i].append(board[i][j])

    result = 0
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 1 :
                if i == 0 or j == 0 :
                    dp[i][j] = 1
                else :
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

            result = max(result, dp[i][j])
    return result**2

print(solution(board))