import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
cut = N * 0.15

# 반올림 함수
def half_ceil(num) :
    if num % 1 < 0.5 :
        num = num // 1
    else :
        num = num // 1 + 1
    return num

arr = []
for _ in range(N) :
    arr.append(int(input()))
arr.sort()

cut = int(half_ceil(cut))
total_cnt = N - (cut*2)

arr = arr[cut:N-cut]

if N == 0 :
    print(0)
else :
    print(int(half_ceil(sum(arr) / total_cnt)))