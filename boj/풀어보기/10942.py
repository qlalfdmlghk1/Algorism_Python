# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = list(map(int,input().split()))
# m = int(input())
# for _ in range(m) :
#     flag = True
#     s,e = map(int, input().split())
#     while s < e :
#         if arr[s-1] != arr[e-1] :
#             flag = False
#             break
#         s += 1
#         e -= 1
#     if not flag:
#         print(0)
#     else :
#         print(1)

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# DP 테이블 초기화
dp = [[False] * n for _ in range(n)]

# 길이 1인 구간 초기화
for i in range(n):
    dp[i][i] = True

# 길이 2인 구간 초기화
for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = True

# 길이 3 이상인 구간에 대한 DP 채우기
for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if arr[i] == arr[j] and dp[i + 1][j - 1]:
            dp[i][j] = True

# 쿼리 처리
for _ in range(m):
    s, e = map(int, input().split())
    if dp[s - 1][e - 1]:
        print(1)
    else:
        print(0)
