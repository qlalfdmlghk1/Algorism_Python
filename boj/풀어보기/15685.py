
n = int(input())

# 2차원 평면을 101x101 크기의 격자로 초기화
graph = [[0] * 101 for _ in range(101)]

# 방향 벡터 (0: 우, 1: 상, 2: 좌, 3: 하)
dx = [0, -1, 0, 1]  # x 방향 이동 (우 -> 상 -> 좌 -> 하)
dy = [1, 0, -1, 0]  # y 방향 이동 (우 -> 상 -> 좌 -> 하)

for i in range(n):
    # 입력: y(세로 좌표), x(가로 좌표), d(시작 방향), g(세대)
    y, x, d, g = map(int, input().split())

    # 드래곤 커브의 시작 좌표를 1로 표시 (커브가 지나는 점)
    graph[x][y] = 1

    curve = [d]

    for j in range(g):
        # 현재 커브를 거꾸로 읽어 90도 회전한 방향을 추가
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)

    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]

        # 좌표가 범위를 벗어나지 않으면 커브 표시
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue
        graph[x][y] = 1

answer = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)
