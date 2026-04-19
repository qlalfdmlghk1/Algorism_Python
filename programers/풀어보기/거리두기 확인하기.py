places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque

def solution(places):
    def bfs(room, r, c):
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        visited = [[False for _ in range(5)] for _ in range(5)]
        q = deque()
        q.append((r, c))
        visited[r][c] = 1
        while q:
            # print(visited)
            print(q)
            cur_r, cur_c = q.popleft()
            for i in range(4):
                nex_r = cur_r + dr[i]
                nex_c = cur_c + dc[i]
                if 0 <= nex_r < 5 and 0 <= nex_c < 5 and visited[nex_r][nex_c] == False and visited[cur_r][cur_c] <= 2 :
                    print(nex_r,nex_c,places[room][nex_r][nex_c])
                    if places[room][nex_r][nex_c] == "P":
                        print("거리두기 지키세요!! answer에 0 저장")
                        return True
                    elif places[room][nex_r][nex_c] == "X":
                        visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
                    else:
                        visited[nex_r][nex_c] = visited[cur_r][cur_c] + 1
                        q.append((nex_r, nex_c))
        return False

    answer = [1, 1, 1, 1, 1]

    def check_distance(room_number) :
        for j in range(5):
            for k in range(5):
                print(places[i][j][k])
                if places[i][j][k] == "P":
                    if bfs(i, j, k):  # 거리두기 안되면 T
                        answer[i] = 0
                        return

    for i in range(5):
        print("room", i)
        check_distance(i)
        print()

    print(answer)


solution(places)
# print(solution(places))
