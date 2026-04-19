n,build_frame = 5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# [x, y, a, b]
# x,y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표
# a는 설치 또는 삭제할 구조물의 종류 (0:기둥, 1:보)
# b는 구조물을 설치할 지, 혹은 삭제할 지 (0:삭제,1:설치)
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제



def solution(n,build_frame):
    answer = []
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

    def check(x, y, a):
        if a == 0 :  # 기둥이면
            if not (graph[y][x] == "b" or graph[y][x] == "c" or y == 0) :
                return False
        elif a == 1 :  # '보'면
            if not (graph[y][x] == "c" or graph[y][x+1] == "c" or (graph[y][x] == "b" and graph[y][x+1] == "b")) : # 아래에 기둥이 없으면
                return False
        return True

    for build in build_frame :
        x,y,a,b = build
        if b == 1 :
            if a == 0 and check(x,y,a) :
                graph[y][x] = "c"
                graph[y+1][x] = "c"
            if a == 1 and check(x,y,a) :
                graph[y][x] = "b"
                graph[y][x+1] = "b"
        else :
            if a == 0 :  # '기둥'이면
                graph[y][x] = 0
                if graph[y+1][x] == 0 : graph[y+1][x] = 0
            else :  # '보'면
                graph[y][x] = 0
                if graph[y][x+1] == 0 : graph[y][x+1] = 0
    return graph
    for i in range(n+1) :
        for j in range(n+1) :
            if graph[i][j] == "c" :
                answer.append([j,i,0])
            elif graph[i][j] == "b" :
                answer.append([j,i,1])
    answer.pop(-1)
    answer.sort()
    return answer

print(solution(n,build_frame))
