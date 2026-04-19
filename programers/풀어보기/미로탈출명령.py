n,m,x,y,r,c,k = 3,3,1,2,3,3,4
# 격자의 크기를 뜻하는 정수 n, m
# 출발 위치를 뜻하는 정수 x, y
# 탈출 지점을 뜻하는 정수 r, c
# 탈출까지 이동해야 하는 거리를 뜻하는 정수 k

from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ""
    graph = [['.' for _ in range(m)]for _ in range(n)]

    def manhattan(x1,y1) :
        return abs(x1 - (r-1)) + abs(y1 - (c-1))

    if manhattan(x-1,y-1) > k or (manhattan(x-1, y-1) - k) % 2:
        return 'impossible'

    for i in range(n) :
        for j in range(m) :
            if i == x-1 and j == y-1 :
                graph[i][j] = "S"
            if i == r-1 and j == c-1 :
                graph[i][j] = "E"

    dr = [1,0,0,-1]  # d l r u
    dc = [0,-1,1,0]

    # def bfs(r,c) :
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == "S" :
                q = deque()
                q.append((i,j,0,""))
                while q :
                    print(q)
                    cur_r,cur_c,cur_cnt,cur_word = q.popleft()
                    for i in range(4) :
                        nex_r = cur_r + dr[i]
                        nex_c = cur_c + dc[i]
                        print(nex_r,nex_c)
                        if 0 <= nex_r < n and 0 <= nex_c < m :
                            if i == 0 :
                                nex_word = cur_word + 'd'
                            if i == 1 :
                                nex_word = cur_word + 'l'
                            if i == 2 :
                                nex_word = cur_word + 'r'
                            if i == 3 :
                                nex_word = cur_word + 'u'

                            nex_cnt = cur_cnt + 1
                            print(nex_cnt)
                            if nex_cnt == k :
                                if graph[nex_r][nex_c] == "E" :
                                    print(nex_word)
                                    exit()
                            if nex_cnt < k :
                                q.append((nex_r,nex_c,nex_cnt,nex_word))
                print("impossible")
solution(3, 3, 1, 2, 3, 3, 4)
    # print(graph)

    # if not answers :
    #     answer = "impossible"
    # else :
    #     answers.sort()
    #     answer = answers[0]
    # return answer


# from collections import deque
# graph = [['.' for _ in range(m)]for _ in range(n)]
#
# for i in range(n) :
#     for j in range(m) :
#         if i == x-1 and j == y-1 :
#             graph[i][j] = "S"
#         if i == r-1 and j == c-1 :
#             graph[i][j] = "E"
#
# dr = [1,-1,0,0]  # d u r l
# dc = [0,0,1,-1]
# answers = []
#
# def bfs(r,c) :
#     global answers
#     q = deque()
#     q.append((r,c,0,""))
#     while q :
#         cur_r,cur_c,cur_cnt,cur_word = q.popleft()
#         for i in range(4) :
#             nex_r = cur_r + dr[i]
#             nex_c = cur_c + dc[i]
#             if 0 <= nex_r < n and 0 <= nex_c < m :
#                 if i == 0 :
#                     nex_word = cur_word + "d"
#                 elif i == 1 :
#                     nex_word = cur_word + "u"
#                 elif i == 2 :
#                     nex_word = cur_word + "r"
#                 elif i == 3 :
#                     nex_word = cur_word + "l"
#
#                 nex_cnt = cur_cnt + 1
#                 if nex_cnt == k :
#                     if graph[nex_r][nex_c] == "E" :
#                         answers.append(nex_word)
#                 elif nex_cnt < k :
#                     q.append((nex_r,nex_c,nex_cnt,nex_word))
# # print(graph)
# for i in range(n) :
#     for j in range(m) :
#         if graph[i][j] == "S" :
#             bfs(i,j)
#
# if not answers :
#     print("impossible")
# else :
#     answers.sort()
#     print(answers[0])