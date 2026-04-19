from collections import deque
dic = dict()
n,m,k = map(int, input().split())
grid = []
for _ in range(n) :
    grid.append(list(input()))

dr = [1,-1,0,0,1,1,-1,-1]
dc = [0,0,1,-1,1,-1,1,-1]

def bfs(r,c) :
    global dic
    q = deque()
    q.append((r,c,grid[r][c]))
    while q :
        cur_r, cur_c, cur_str = q.popleft()
        for i in range(8) :
            nex_r,nex_c = cur_r + dr[i], cur_c + dc[i]
            if nex_r >= n :
                nex_r -= n
            if nex_r < 0 :
                nex_r += n
            if nex_c >= m:
                nex_c -= m
            if nex_c < 0 :
                nex_c += m

            nex_str = cur_str + grid[nex_r][nex_c]
            if len(nex_str) <= 5 :
                q.append((nex_r,nex_c,nex_str))
                if nex_str in dic :
                    dic[nex_str] += 1
                else :
                    dic[nex_str] = 1

for i in range(n) :
    for j in range(m) :
        if grid[i][j] not in dic :
            dic[grid[i][j]] = 1
        else :
            dic[grid[i][j]] += 1
        bfs(i,j)

for _ in range(k) :
    god_word = input()
    if god_word not in dic :
        print(0)
    else :
        print(dic[god_word])