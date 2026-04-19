from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
answer = defaultdict()

arr = list(map(int, input().split()))
new_array = []

# 입력받은 숫자의 최대값
max_num = max(arr)

for i, num in enumerate(arr):
    answer[num] = 0
    new_array.append((i,num))

# 입력받은 숫자를 작은 수대로 정렬함.
new_array.sort(key=lambda x: x[1])

for li in range(n):
    index, num = new_array[li]

    # 에라토스테네스의 체
    # target은 num의 배수
    for target in range(num * 2, max_num + 1, num):

        # target이 만약 num에 등장한 값이라면 비교.
        # target은 num의 배수이므로 무조건 target % num == 0 임.
        if target in answer:
            answer[num] += 1
            answer[target] -= 1

# dictionary 자료구조가 파이썬 3.6 이상에선 입력받은 순서를 기억한다고 함.
for key, item in answer.items():
    print(item, end=" ")