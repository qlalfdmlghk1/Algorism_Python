import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split(' ')))

left = 0
right = n - 1

solutions.sort()   # 이분탐색을 하기 위해 정렬

answer = abs(solutions[left] + solutions[right])
final = [solutions[left], solutions[right]]      # 최종 두 용액을 담을 배열

# 투 포인터
while left < right:
    left_val = solutions[left]
    right_val = solutions[right]

    sum = left_val + right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:    # 0 이면 바로 break
            break
    # 두 값의 합이 0보다 작으면 -> left 포인터를 오른쪽으로 이동
    if sum < 0:
        left += 1
    # 두 값의 합이 0보다 크면 -> right 포인터를 왼쪽으로 이동
    else:
        right -= 1

print(final[0], final[1])