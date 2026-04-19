import sys
input = sys.stdin.readline
from heapq import heappush,heappop

def bf():
    # inf를 사용하지 않고 임의의 큰 수 사용
    D = [200000000] * (N+1)
    # 어느 점을 기준으로 해도 상관없음
    D[1] = 0

    # N번 검사
    for i in range(N):
        for rou in route:
            start, goal, time = rou
            if D[goal] > D[start] + time:
                D[goal] = D[start] + time
                # N번 시행시 갱신된다면, 음의 가중치 판단.
                if i == N-1:
                    return 'YES'
    return 'NO'


# 변수 입력
TC = int(input())

for _ in range(TC):
    N, M, W = map(int,input().split())
    route = []
    for _ in range(M):
        a, b, t = map(int,input().split())
        route.append([a,b,t])
        route.append([b,a,t])

    for _ in range(W):
        s, e, t = map(int,input().split())
        route.append([s,e,-t])


    print(bf())


# tc = int(input())
# # 지점의 수 N, 도로의 개수 M, 웜홀의 개수 W
# for _ in range(tc) :
#     n, m, w = map(int, input().split())
#     graph = [[] for _ in range(n + 1)]
#     for _ in range(m) :
#         s1,e1,t1 = map(int,input().split())
#         graph[s1].append((t1,e1))
#         graph[e1].append((t1,s1))
#     for _ in range(w) :
#         s2,e2,t2 = map(int,input().split())
#         graph[s2].append((-1*t2,e2))
    # def dikstra(start) :
    #     pq = []
    #     pq.append((0,start))
    #     # distance[start] = 0
    #     while pq :
    #         if distance[start] < 0 :
    #             return True
    #         cur_distance, cur_node = heappop(pq)
    #         if distance[cur_node] < cur_distance :
    #             continue
    #         for next_distance,next_node in graph[cur_node] :
    #             sum_distance = cur_distance + next_distance
    #             if distance[next_node] > sum_distance :
    #                 distance[next_node] = sum_distance
    #                 heappush(pq,(sum_distance,next_node))
    #     return False
    #
    # total = []
    # for i in range(1,n+1) :
    #     total.append(dikstra(i))
    #
    # if True in total :
    #     print("YES")
    # else :
    #     print("NO")