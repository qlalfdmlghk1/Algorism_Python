land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
# result = 9
from collections import deque
from collections import defaultdict
r = len(land)
c = len(land[0])

dr = [1,-1,0,0]
dc = [0,0,1,-1]

visited = [[False for _ in range(c)] for _ in range(r)]
oil_dic = defaultdict(int)

def bfs(y,x) :
    cnt = 0
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    land[y][x] = oil_count
    cnt += 1
    while q :
        cur_r, cur_c = q.popleft()
        for i in range(4) :
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if (0 <= next_r < r and 0 <= next_c < c and
                    visited[next_r][next_c] == False and land[next_r][next_c] == 1):
                visited[next_r][next_c] = True
                land[next_r][next_c] = oil_count
                q.append((next_r,next_c))
                cnt += 1
    return cnt

oil_count = 2
for i in range(r) :
    for j in range(c) :
        if land[i][j] == 1 :
            oil_dic[oil_count] = bfs(i,j)
            oil_count += 1

answer = 0
for i in range(c) :
    result = 0
    oil_type = set(land[j][i] for j in range(r))
    for type in oil_type :
        result += oil_dic[type]
    answer = max(result, answer)
print(answer)

# total = []
# for i in range(c) :
#     result = 0
#     visited = [[False for _ in range(c)] for _ in range(r) ]
#     for j in range(r) :
#         if land[j][i] == 1 and visited[j][i] == False:
#             result += bfs(j,i)
#     total.append(result)
# print(max(total))
