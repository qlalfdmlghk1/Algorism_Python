n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
safe_zone = 0


def dfs(r, c):
    global safe_zone

    # 현재 위치 방문처리
    visited[c][r] = True
    # 사이클에 현재 위치 추가
    cycle.append((r, c))

    if grid[c][r] == 'U' and c > 0:        # 위로
        c -= 1
    elif grid[c][r] == 'D' and r < n - 1:  # 아래
        c += 1
    elif grid[c][r] == 'L' and r > 0:      # 왼쪽
        r -= 1
    elif grid[c][r] == 'R' and r < m - 1:  # 오른쪽
        r += 1

    if visited[c][r]:         # 이동한 위치를 이미 방문한 경우
        if (c, r) in cycle:   # 사이클에 이 위치가 포함되어 있다면
            safe_zone += 1    # 사이클이 생겼으므로 세이프 존을 설치해야한다.
    else:                     # 방문안했으면 다음 위치로
        dfs(r, c)


for i in range(m):
    for j in range(n):
        if not visited[j][i]:
            cycle = []
            dfs(i, j)

print(safe_zone)