# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고,
# 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상('*'), 아차상('#')이 존재.
# 스타상('*') 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배. 아차상('#') 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성
# 입력 형식 : "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.
# 출력 형식 : 3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력
dartResult = '1D2S3T*'	#answer =37, 설명   : 1 * 2 + 4 * 2 + 27
dic = {'S':True,'D':True,'T':True}
dic2 = {'*':True, '#':True}
stack = []
for i in dartResult :
    # print(stack)
    if i in dic :
        if i == 'S' :
            cur = stack.pop()
            stack.append(cur)
            # continue
        elif i == 'D' :
            cur = stack.pop()
            stack.append(cur ** 2)
            # continue
        else :
            cur = stack.pop()
            stack.append(cur ** 3)
            # continue
    elif i in dic2:
        if stack and i == '*':
            cur = stack.pop()
            if stack :
                before = stack.pop()
                stack.append(before*2)
            stack.append(cur * 2)
            # continue
        elif stack and i == '#' :
            cur = stack.pop()
            stack.append(cur * -1)
            # continue
    else :
        if stack and stack[-1] == 1 and i == '0' :
            stack.pop()
            stack.append(10)
        else :
            stack.append(int(i))
print(sum(stack))