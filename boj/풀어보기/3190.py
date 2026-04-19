from collections import deque

n = int(input())
k = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1  # 입력은 1부터 시작하므로 인덱스를 맞추기 위해 -1

l = int(input())
dic = {}
for _ in range(l):
    x, c = input().split()
    dic[int(x)] = c

time = 0
direction = 0        # 처음에는 오른쪽
cur_r, cur_c = 0, 0  # 뱀의 시작 위치 (0, 0)
snake = deque([(cur_r, cur_c)])  # 뱀의 몸 위치를 deque로 관리
graph[cur_r][cur_c] = 2  # 뱀이 있는 위치는 2로 표시

# 방향 벡터 (동, 남, 서, 북)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while True:
    time += 1
    # 새로운 머리 위치
    cur_r += dr[direction]
    cur_c += dc[direction]

    # 벽에 부딪히거나 뱀의 몸에 부딪히면 게임 종료
    if cur_r < 0 or cur_r >= n or cur_c < 0 or cur_c >= n or graph[cur_r][cur_c] == 2:
        break

    # 사과가 있으면
    if graph[cur_r][cur_c] == 1:
        graph[cur_r][cur_c] = 2  # 뱀의 머리 위치 갱신
        snake.append((cur_r, cur_c))  # 뱀의 몸길이 늘리기
    else:
        # 사과가 없으면
        graph[cur_r][cur_c] = 2  # 뱀의 머리 위치 갱신
        snake.append((cur_r, cur_c))
        tail_r, tail_c = snake.popleft()  # 꼬리 제거
        graph[tail_r][tail_c] = 0  # 꼬리가 있던 자리 비우기

    # 시간이 되었을 때 방향 전환
    if time in dic:
        if dic[time] == 'L':
            direction = (direction - 1) % 4  # 왼쪽으로 90도 회전
        elif dic[time] == 'D':
            direction = (direction + 1) % 4  # 오른쪽으로 90도 회전

print(time)