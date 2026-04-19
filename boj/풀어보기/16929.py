from collections import deque
n,m = map(int,input().split())
graph = []
for _ in range(n) :
    graph.append(list(input()))

visited = [[False for _ in range(m)] for _ in range(n)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def is_circle(r,c) :
    parent = {}
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    parent[(r,c)] = (-1,-1) # 시작점은 없음
    board_alpha = graph[r][c]
    while q :
        cur_r,cur_c = q.popleft()
        for i in range(4) :
            nex_r = dr[i] + cur_r
            nex_c = dc[i] + cur_c

            # 범위 먼저 확인
            if not (0 <= nex_r < n and 0 <= nex_c < m):
                continue

            # 같은 알파벳일 때만 탐색
            if graph[nex_r][nex_c] != board_alpha:
                continue

            # 이미 방문한 칸이라면 사이클인지 확인
            if visited[nex_r][nex_c] :
                if parent[(cur_r,cur_c)] != (nex_r,nex_c) :
                    return True
                continue

            # 새롭게 방문했다면
            visited[nex_r][nex_c] = True
            parent[(nex_r,nex_c)] = (cur_r,cur_c)
            q.append((nex_r,nex_c))
    return False


def check() :
    for i in range(n) :
        for j in range(m) :
            if not visited[i][j] :
                if is_circle(i,j) :
                    return "Yes"
    return "No"

print(check())




