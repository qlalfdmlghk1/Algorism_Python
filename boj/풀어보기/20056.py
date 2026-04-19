n,m,k = map(int, input().split())  # n x n, 파이어볼 m개, 명령 k번

balls = []

for _ in range(m) :
    r,c,w,s,d = map(int, input().split())  # (r,c), 질량 w, 방향 d, 속력 s
    balls.append((r-1,c-1,w,s,d))

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

for _ in range(k) :
    new_graph = [[[] for _ in range(n)] for _ in range(n)]

    # 3-1. 파이어볼 이동
    for r,c,w,s,d in balls :
        nex_r = (r + dr[d] * s) % n  # 넘어가는 것 고려
        nex_c = (c + dc[d] * s) % n
        new_graph[nex_r][nex_c].append([w,s,d])
    balls = []

    # 3-2. 파이어볼 합치고 나누기
    for r in range(n) :
        for c in range(n) :
            # 파이어볼 없는 경우
            if len(new_graph[r][c]) == 0 :
                continue
            # 파이어볼 1개
            if len(new_graph[r][c]) == 1 :
                balls.append([r,c] + new_graph[r][c][0])  # [2, 3] + [5, 1, 2] -> [2, 3, 5, 1, 2]
            # 파이어볼 2개 이상
            else :
                sum_w = sum(x[0] for x in new_graph[r][c])
                sum_s = sum(s[1] for s in new_graph[r][c])
                count = len(new_graph[r][c])  # 파이어볼 개수
                dirs = [x[2] % 2 for x in new_graph[r][c]]  # 방향의 홀짝

                if all(d == dirs[0] for d in dirs):
                    new_dirs = [0, 2, 4, 6]  # 전부 짝수 or 전부 홀수
                else:
                    new_dirs = [1, 3, 5, 7]

                if sum_w // 5 > 0 :
                    for d in new_dirs :
                        balls.append([r,c,sum_w // 5, sum_s // count, d])

print(sum(ball[2] for ball in balls))