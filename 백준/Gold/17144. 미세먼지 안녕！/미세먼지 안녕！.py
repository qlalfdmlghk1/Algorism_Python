r,c,t = map(int,input().split())
graph = []

for _ in range(r) :
    graph.append(list(map(int,input().split())))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

# 공기청정기 위치
for i in range(r) :
    if graph[i][0] == -1 :
        a1 = i
        break
a2 = i + 1

# 미세먼지 확산 함수
def spread(new_graph,cr,cc) :
    cnt = 0  # 확산된 방향의 개수
    for i in range(4) :
        nr, nc = cr + dr[i], cc + dc[i]
        if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] != -1 :
            cnt += 1
            new_graph[nr][nc] += graph[cr][cc] // 5
    new_graph[cr][cc] += graph[cr][cc] - ((graph[cr][cc] // 5) * cnt)

# 공기청정기 작동
def cleaning(new_graph,a1,a2) :
    # 윗 회전 (반시계)
    up_list = []
    for j in range(c-1) :
        up_list.append(new_graph[a1][j])
    for i in range(a1,0,-1) :
        up_list.append(new_graph[i][c-1])
    for j in range(c-1,0,-1) :
        up_list.append(new_graph[0][j])
    for i in range(0,a1) :
        up_list.append(new_graph[i][0])

    up_list.pop(-1)

    for j in range(1,c-1) :
        new_graph[a1][j] = up_list.pop(0)
    for i in range(a1,0,-1) :
        new_graph[i][c-1] = up_list.pop(0)
    for j in range(c-1,0,-1) :
        new_graph[0][j] = up_list.pop(0)
    for i in range(0,a1) :
        new_graph[i][0] = up_list.pop(0)


    # 아랫 회전 (반시계)
    down_list = []
    for j in range(c-1) :
        down_list.append(new_graph[a2][j])
    for i in range(a2,r-1) :
        down_list.append(new_graph[i][c-1])
    for j in range(c-1,0,-1) :
        down_list.append(new_graph[r-1][j])
    for i in range(r-1,a2,-1) :
        down_list.append(new_graph[i][0])

    down_list.pop(-1)

    for j in range(1,c-1) :
        new_graph[a2][j] = down_list.pop(0)
    for i in range(a2,r-1) :
        new_graph[i][c-1] = down_list.pop(0)
    for j in range(c-1,0,-1) :
        new_graph[r-1][j] = down_list.pop(0)
    for i in range(r-1,a2,-1) :
        new_graph[i][0] = down_list.pop(0)

for _ in range(t) :
    new_graph = [[0 for _ in range(c)]  for _ in range(r)]
    for i in range(r) : 
        for j in range(c) :
            if graph[i][j] > 0 :
                spread(new_graph,i,j)

    cleaning(new_graph,a1,a2)
    graph = new_graph
    graph[a1][0],graph[a2][0] = -1,-1

answer = 2


for g in graph :
    answer += sum(g)
print(answer)