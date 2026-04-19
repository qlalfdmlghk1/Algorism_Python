from collections import deque

n,m,k = map(int,input().split())  # (1,1) ~ (n,m)까지 최대 k개 벽 부실 수 있음
graph = []
for _ in range(n) :
    graph.append(list(map(int,input())))

dr = [1,-1,0,0]
dc = [0,0,1,-1]
visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

# print(graph)
# print(visited)

def range_check(r,c) :
    if 0 <= r < n and 0 <= c < m  :
        return True
    return False

def bfs() :
    q = deque()
    q.append((0,0,k))
    visited[0][0][k] = 1
    while q :
        cur_r,cur_c,cur_cnt = q.popleft()
        if cur_r == n-1 and cur_c == m-1 :
            return visited[cur_r][cur_c][cur_cnt]

        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            # 벽 안 부수기
            if range_check(nex_r,nex_c) :
                if not visited[nex_r][nex_c][cur_cnt] and graph[nex_r][nex_c] == 0 :
                    nex_cnt = cur_cnt
                    visited[nex_r][nex_c][nex_cnt] = visited[cur_r][cur_c][cur_cnt] + 1
                    q.append((nex_r,nex_c,nex_cnt))

            # 벽 부수기
                elif cur_cnt >= 1 and not visited[nex_r][nex_c][cur_cnt-1] and graph[nex_r][nex_c] == 1 :
                    nex_cnt = cur_cnt - 1
                    visited[nex_r][nex_c][nex_cnt] = visited[cur_r][cur_c][cur_cnt] + 1
                    q.append((nex_r,nex_c,nex_cnt))
    return -1

print(bfs())