import copy

n,m = map(int, input().split())
board = []
cctv = []
for i in range(n) :
    board.append(list(map(int,input().split())))
    for j in range(m) :
        if 1 <= board[i][j] <= 5 :
            cctv.append((i,j,board[i][j]))

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
cctv_dir = {
    1 : [[0],[1],[2],[3]],
    2 : [[0,2], [1,3]],
    3 : [[0,1], [1,2], [2,3], [3,0]],
    4 : [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5 : [[0,1,2,3]]
}


# 한 방향으로 감시를 진행하는 함수
def watch(temp_map,r,c,d) :
    nex_r = r + dirs[d][0]
    nex_c = c + dirs[d][1]
    while 0 <= nex_r < n and 0 <= nex_c < m :
        if temp_map[nex_r][nex_c] == 6 :
            break
        if temp_map[nex_r][nex_c] == 0 : # 빈칸인 경우
            temp_map[nex_r][nex_c] = "#"
        nex_r += dirs[d][0]
        nex_c += dirs[d][1]

result = int(1e9)
# 백트래킹 -> 모든 CCTV 방향 조합 탐색
def dfs(depth, cur_map) :
    global result
    if depth == len(cctv) :  # 모든 cctv 방향 결정했으면
        count = 0
        for row in cur_map :
            count += row.count(0)
        result = min(result, count)
        return

    cur_r, cur_c, cctv_type = cctv[depth]
    for dir in cctv_dir[cctv_type] :
        copy_map = copy.deepcopy(cur_map)  # GPT 형님 잘 배워 갑니다.
        for d in dir :
            watch(copy_map,cur_r,cur_c,d)
        dfs(depth+1, copy_map)


dfs(0,board)

print(result)
