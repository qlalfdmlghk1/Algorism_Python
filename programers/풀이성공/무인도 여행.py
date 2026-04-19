maps = ["XXX","XXX","XXX"]

from collections import deque
def solution(maps):
    answer = []
    n,m = len(maps),len(maps[0])
    visited = [[False for i in range(m)] for i in range(n)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    def check_island(r,c) :
        day = int(maps[r][c])
        q = deque()
        q.append((r,c))
        visited[r][c] = True
        while q :
            cur_r, cur_c = q.popleft()
            for i in range(4) :
                nex_r = cur_r + dr[i]
                nex_c = cur_c + dc[i]
                if 0 <= nex_r < n and 0 <= nex_c < m and not visited[nex_r][nex_c] and maps[nex_r][nex_c] != "X" :
                    q.append((nex_r,nex_c))
                    visited[nex_r][nex_c] = True
                    day += int(maps[nex_r][nex_c])
        answer.append(day)

    for i in range(n) :
        for j in range(m) :
            if maps[i][j] != "X" and not visited[i][j]:
                check_island(i,j)

    if not answer :
        answer.append(-1)

    answer.sort()
    return answer

print(solution(maps))