from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]

# 가장 먼저 해야할 일 : 섬들에게 번호를 부여 -> 인접한 땅은 동일한 섬에 소속되어야 함 => BFS
def bfs(r,c,island) :
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    q = deque()
    q.append((r,c))
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(4) :
            nex_r = cur_r + dr[i]
            nex_c = cur_c + dc[i]
            if 0 <= nex_r < n and 0 <= nex_c < m and graph[nex_r][nex_c] == 1 and visited[nex_r][nex_c] == False :
                visited[nex_r][nex_c] = True
                graph[nex_r][nex_c] = island
                q.append((nex_r,nex_c))

islandNum = 2
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 and visited[i][j] == False :
            bfs(i,j,islandNum)
            islandNum += 1
print(graph)


# 다음으로 할 일 : 섬들을 연결하는 다리 만들기 -> 섬을 연결할 때, 한 방향으로만 다리를 만들어나가야 함
bridge = []



# 다리 연결이 조건을 만족하면 다리에 연결된 섬번호와 다리의 길이를 리스트에 추가
# 이후 MST(최소 신장 트리)로 해결한다.
# MST에서 선택된 다리의 개수가 섬의 개수 -1 이 아니라면 모든 섬이 연결되지 않은 것 => -1 출력
