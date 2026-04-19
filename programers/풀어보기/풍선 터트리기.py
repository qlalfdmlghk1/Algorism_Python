a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
from itertools import combinations

def solution(a):
    # 총 len(a)-1 번 터트릴 수 있음 -> 그 중에 한 번만 앞 풍선 터트릴 수 있음
    answer = 2
    dp = []
    for _ in range(2) :
        dp.append([0 for _ in range(len(a))])

    dp[0][0] = a[0]
    dp[1][-1] = a[-1]

    # 좌측->우측 방향 최솟값dp
    for i in range(1, len(a)):
        dp[0][i] = min(dp[0][i - 1], a[i])
    # 우측->좌측 방향 최솟값dp
    for i in range(len(a) - 2, -1, -1):
        dp[1][i] = min(dp[1][i+1],a[i])

    for i in range(1, len(a) - 1):
        left_min = dp[0][i - 1]  # 좌측 최솟값
        right_min = dp[1][i + 1]  # 우측 최솟값
        # 양쪽 모두 큰경우
        if left_min > a[i] and right_min > a[i]:
            answer += 1
        # 한쪽은 크고 다른한쪽은 작은경우
        elif (left_min > a[i] and right_min < a[i]) or (left_min < a[i] and right_min > a[i]):
            answer += 1

print(solution(a))