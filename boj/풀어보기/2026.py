import sys
input = sys.stdin.readline

from itertools import combinations

k, n, f = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]  # 친구 관계 저장

for _ in range(f) :
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 후보 조합을 오름차순으로 만들어봄
for friends in combinations(range(1, n+1), k):  # n명 중 k명 고르기
    is_all_friend = True  # 모두가 친구인가
    for i in range(k) :
        for j in range(i+1, k) :
            a, b = friends[i], friends[j]
            if not graph[a][b] :  # 친구가 아니면 탈락
                is_all_friend = False
                break
        if not is_all_friend:
            break

    if is_all_friend :
        for x in friends :
            print(x)
        sys.exit()

print(-1)
