percent = list(map(int, input().split()))
n = percent.pop(0)

visited = [[False for _ in range(2*n+1)] for _ in range(2*n+1)]
print(percent)
answer = 0

def dfs (r,c,per,cnt) :
    global answer
    if cnt == n :
        answer += per
        return
    else :
        dr = [0, 0, 1, -1]  # 동 서 남 북 으로 이동
        dc = [1, -1, 0, 0]
        for i in range(4) :
            nex_r = r + dr[i]
            nex_c = c + dc[i]
            if 0 <= nex_r < (2*n+1) and 0 <= nex_c < (2*n+1) :
                if visited[nex_r][nex_c] :  # 이미 방문한 지점 다시 방문하면 -> 단순x
                    continue                # 그 위치로 가지 않음
                else :
                    visited[nex_r][nex_c] = True
                    nex_per = per * (percent[i] / 100)
                    dfs(nex_r, nex_c, nex_per, cnt+1)  # 진행함
                    visited[nex_r][nex_c] = False

visited[n][n] = True
dfs (n,n,1,0)
print(answer)