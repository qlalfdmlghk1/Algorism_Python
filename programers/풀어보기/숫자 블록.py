begin,end = 1,10

def solution(begin, end):
    answer = []

    for i in range(begin,end+1) :
        if i == 1 :
            answer.append(0)
            continue

        max_divisor = 1  # 가장 큰 약수
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                # 가장 큰 약수 저장
                quotient = i // j
                if quotient <= 10 ** 7:
                    max_divisor = quotient
                    break
                else:
                    max_divisor = j  # 나누는 수가 작을 경우엔 j가 더 작을 수도 있음
        answer.append(max_divisor)
    return answer



print(solution(begin,end))