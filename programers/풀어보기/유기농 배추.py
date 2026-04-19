# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.
#
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.



'''for _ in range(t) :
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    # print(graph)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cnt = 0

    def dfs(y, x):
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            if 0 <= next_x < m and 0 <= next_y < n and graph[next_y][next_x] == 1 and visited[next_y][next_x] == False:
                graph[next_y][next_x] = 1
                visited[next_y][next_x] = True
                dfs(next_y, next_x)


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False :
                dfs(i, j)
                cnt += 1
    print(cnt)'''

from collections import deque
q = deque()
t = int(input())
for _ in range(t) :
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cnt = 0

    def bfs(y, x):
        q.append((y,x))
        while q :
            cur_y, cur_x = q.popleft()
            for i in range(4):
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                if 0 <= next_x < m and 0 <= next_y < n and graph[next_y][next_x] == 1 and visited[next_y][next_x] == False:
                    visited[next_y][next_x] = True
                    q.append((next_y,next_x))


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False :
                bfs(i, j)
                cnt += 1
    print(cnt)