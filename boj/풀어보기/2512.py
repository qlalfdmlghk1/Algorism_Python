n = int(input())
budget = list(map(int, input().split()))
maxi = int(input())

budget.sort()
left = 1
right = budget[-1]

answer = 0  # 최적의 상한값 저장

while left <= right:  # 범위 조건 수정
    mid = (left + right) // 2
    total = 0

    for b in budget:
        if b > mid:
            total += mid
        else:
            total += b

    if total <= maxi:       # 총 예산이 허용 금액보다 작거나 같다면
        answer = mid        # 가능한 상한값 업데이트  ->  여기가 키 포인트네
        left = mid + 1      # 더 높은 값을 탐색
    else:                   # 총 예산이 허용 금액보다 크다면
        right = mid - 1     # 더 낮은 값을 탐색

print(answer)               # 최적의 상한값 출력