money = [1,2,3,1]

def solution(money):
    answer = 0
    length = len(money)
    dp1 = [0] * length
    dp2 = [0] * length

    # 첫번째 집 선택한 경우
    dp1[0] = money[0]
    for i in range(1,length-1) : # 원이니까, 마지막 집은 선택을 못함
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # 첫번째 선택 안한 경우
    dp2[0] = 0
    for i in range(1, length):  # 원이니까, 마지막 집은 선택을 못함
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    answer = max(dp1[-2], dp2[-1])
    return answer

print(solution(money))