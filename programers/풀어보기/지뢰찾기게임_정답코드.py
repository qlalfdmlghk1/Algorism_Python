board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1,2]
from collections import deque
# 시작지점이 지뢰인 경우
if board[click[0]][click[1]] == 'M':
    board[click[0]][click[1]] = 'X'
    print(board)

visited = set()
queue = deque([click])
visited.add(frozenset([(click[0], click[1])]))
n, m = len(board), len(board[0])

# 유효한 방향 검사
def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

# 지뢰 개수 확인
def check_mine(r, c):
    mine_count = 0
    for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        next_r, next_c = r + dr, c + dc
        if in_range(next_r, next_c):
            if board[next_r][next_c] == 'M':
                mine_count += 1
    print(mine_count)

while queue:
    cur_r, cur_c = queue.popleft()

    # E인 경우 지뢰 개수 확인 후 B or 1~8숫자로 변환
    if board[cur_r][cur_c] == 'E':
        mine_count = check_mine(cur_r, cur_c)
        if mine_count:
            board[cur_r][cur_c] = str(mine_count)
        else:
            board[cur_r][cur_c] = 'B'

    # 지뢰인 경우 continue
    elif board[cur_r][cur_c] == 'M':
        continue

    for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        next_r, next_c = cur_r + dr, cur_c + dc
        if in_range(next_r, next_c) and frozenset([(next_r, next_c)]) not in visited and board[cur_r][
                    cur_c] == 'B':
            queue.append([next_r, next_c])
            visited.add(frozenset([(next_r, next_c)]))
print(board)