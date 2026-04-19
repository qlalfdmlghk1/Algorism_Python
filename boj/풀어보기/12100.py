import sys, copy
n = int(input())
grid = []  # 초기 보드 상태
ans = 0

for _ in range(n):
    grid.append(list(map(int,input().split())))

def left(board):
    for i in range(n):
        cursor = 0                  # 합칠 위치
        for j in range(1, n):
            if board[i][j] != 0:    # 현재 위치에 숫자가 있으면
                tmp = board[i][j]   # tmp에 숫자를 저장
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp     # 숫자를 왼쪽으로 이동

                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2      # 같은 숫자 합침
                    cursor += 1                # 다음 위치로 이동
                else:
                    cursor += 1
                    board[i][cursor] = tmp     # 숫자를 현재 위치에 놓음
    return board

def right(board):
    for i in range(n):
        cursor = n - 1
        for j in range(n - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp

                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def up(board):
    for j in range(n):
        cursor = 0
        for i in range(n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down(board):
    for j in range(n):
        cursor = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

def dfs(depth, arr):
    global ans
    if depth == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        copy_arr = [row[:] for row in arr]  # 깊은 복사 수행 -> 각 재귀 호출마다 독립적인 보드 상태를 유지
        if i == 0:
            dfs(depth + 1, left(copy_arr))
        elif i == 1:
            dfs(depth + 1, right(copy_arr))
        elif i == 2:
            dfs(depth + 1, up(copy_arr))
        else:
            dfs(depth + 1, down(copy_arr))

dfs(0, grid)
print(ans)
