def check(idx):
    # 주어진 인덱스 idx에 비숍을 놓을 수 있는지 확인하는 함수
    # c는 짝수(0) 또는 홀수(1)를 나타내는 변수
    c = idx % 2
    i, j = idx // n, idx % n  # i, j는 idx를 통해 얻는 행과 열의 위치

    # 네 방향(대각선)으로 비숍을 놓을 수 있는지 확인
    for d in range(4):
        x, y = i + dx[d], j + dy[d]
        while 0 <= x < n and 0 <= y < n:  # 체스판 내부에서 반복
            if visited[x * n + y]:  # 다른 비숍과 충돌할 경우 False 반환
                return False
            x += dx[d]
            y += dy[d]
    return True  # 충돌이 없을 경우 True 반환

def dfs(idx, c, cnt):
    # 백트래킹 방식으로 가능한 비숍 배치 경우의 수를 찾는 함수
    if n * n - idx + 1 + cnt <= ans[c] or idx >= n * n:
        # 남은 칸으로 더 많은 비숍을 놓을 수 없거나 인덱스가 범위를 넘어가면 종료
        return

    ans[c] = max(ans[c], cnt)  # 현재까지 놓은 비숍의 최대 개수를 갱신
    x, y = idx // n, idx % n  # 현재 인덱스를 기반으로 행과 열 계산
    j = y

    for i in range(x, n):  # 행을 이동하면서 가능한 위치 찾기
        while j < n:  # 현재 행에서 가능한 위치 탐색
            v = i * n + j
            if not visited[v] and chess[i][j] == 1 and check(v):  # 비숍을 놓을 수 있는지 확인
                visited[v] = True   # 비숍을 놓음
                dfs(v, c, cnt + 1)  # 다음 비숍 위치로 이동
                visited[v] = False  # 탐색 후 비숍 위치를 초기화
            j += 2  # 같은 색의 다음 칸으로 이동
        if i % 2 == 0 :
            j = (c + 1) % 2
        else :
            j = c  # 다음 행의 시작 열을 설정


n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 1, -1]
dy = [1, 1, -1, -1]
visited = [[False for _ in range(n)] for _ in range(n)]
ans = [0, 0]  # 짝수 색과 홀수 색에서 놓을 수 있는 비숍의 최대 개수

dfs(0, 0, 0)
dfs(1, 1, 0)

print(sum(ans))