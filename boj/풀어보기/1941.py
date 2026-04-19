from collections import deque

graph = []
for _ in range(5) :
    graph.append(list(input()))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(r,c) :
    cnt_s, cnt_y, cnt = 0,0,0
    if graph[r][c] == "S" : cnt_s += 1
    if graph[r][c] == "Y" : cnt_y += 1
    q = deque()
    q.append((r,c))
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[r][c] = True
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(4) :
            nex_r = dr[i] + cur_r
            nex_c = dc[i] + cur_c
            if 0 <= nex_r < 5 and 0 <= nex_c < 5 and not visited[nex_r][nex_c] :
                if graph[nex_r][nex_c] == "S" and cnt_y + cnt_s <= 6 :
                    cnt_s += 1
                    q.append((nex_r, nex_c))
                if graph[nex_r][nex_c] == "Y" and cnt_y < 3 and cnt_y + cnt_s <= 6 :
                    cnt_y += 1
                    q.append((nex_r,nex_c))

                print(nex_r,nex_c, "||" , cnt_s,cnt_y)
                if cnt_s + cnt_y == 7 :
                    cnt += 1
    return cnt

result = 0
for i in range(5) :
    for j in range(5) :
        if graph[i][j] == "S" :
            result += bfs(i,j)
            print("다음 S")
print(result)