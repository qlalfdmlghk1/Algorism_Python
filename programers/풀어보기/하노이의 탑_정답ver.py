n = 2

def hanoi(n, From, Toward, Sub):
    if n == 1:
        answer.append([From, Toward])
        return
    hanoi(n - 1, From, Sub, Toward)  # n-1개의 원반을 Sub 기둥을 이용하여 From 기둥에서 Toward 기둥으로 옮기는 작업
    answer.append([From, Toward])    # 남아 있는 가장 큰 원반을 목표 기둥으로 옮깁니다.
    hanoi(n - 1, Sub, Toward, From)  # Sub 기둥에 임시로 옮겨둔 n-1개의 원반을 최종 목적지인 Toward 기둥으로 옮기기 위해 재귀적으로 호출

answer = []
hanoi(n, 1, 3, 2)
print(answer)