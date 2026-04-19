board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1,2]
from collections import deque

# 시작지점이 지뢰인 경우
if board[click[0]][click[1]] == 'M':
    board[click[0]][click[1]] = 'X'
    print(board)

visited = set()
q = deque([click])
visited.add(frozenset([(click[0], click[1])]))
n, m = len(board), len(board[0])


# 지뢰 개수 확인
def check(r, c):
    cnt = 0
    for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        next_r, next_c = r + dr, c + dc
        if 0 <= next_r < n and 0 <= next_c < m :
            if board[next_r][next_c] == 'M':
                cnt += 1
    print(cnt)

while q:
    cur_r, cur_c = q.popleft()

    # E인 경우 지뢰 개수 확인 후 B or 1~8숫자로 변환
    if board[cur_r][cur_c] == 'E':
        cnt = check(cur_r, cur_c)
        if cnt:
            board[cur_r][cur_c] = str(cnt)
        else:
            board[cur_r][cur_c] = 'B'

    # 지뢰인 경우 continue
    elif board[cur_r][cur_c] == 'M':
        continue

    dr = [0,1,1,1,0,-1,-1,-1]
    dc = [1,1,0,-1,-1,-1,0,1]
    for i in range(8) :
        next_r, next_c = cur_r + dr[i], cur_c + dc[i]
        if 0 <= next_r < n and 0 <= next_c < m and frozenset([(next_r, next_c)]) not in visited and board[cur_r][
                    cur_c] == 'B':
            q.append([next_r, next_c])
            visited.add(frozenset([(next_r, next_c)]))
print(board)