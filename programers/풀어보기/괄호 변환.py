p = "(()())()" # (())()(())
# ( 개수 == ) 개수 : 균형잡힌 괄호 문자열
# () 짝 맞으면 : 올바른 괄호 문자열

def solution(p):
    p = list(p)
    answer = ''

    # 1번 (입력이 빈 문자열인 경우)
    if not p :
        return answer

    # 2번
    u = []
    check = []
    left_cnt, right_cnt = 0,0
    while True :
        cur = p.pop(0)
        u.append(cur)

        if check and check[-1] == '(' and cur == ')' :
            check.pop(-1)
        else :
            check.append(cur)

        if cur == "(" :
            left_cnt += 1
        elif cur == ")" :
            right_cnt += 1

        # 올바른 괄호 문자열인지 체크해야 함
        if left_cnt == right_cnt :
            break

    v = p

    # 3번 (u가 올바른 괄호 문자열이라면)
    if not check :
        for i in u :
            answer += i
        # 1번부터 돌리기
        answer += solution(v)
        return answer

    # 4번 (u가 올바른 괄호 문자열이 아니라면)
    if check :
        answer += '('
        answer += solution(v)
        answer += ')'
        u.pop(0)
        u.pop(-1)
        for i in u :
            if i == '(' :
                answer += ')'
            else :
                answer += '('
        return answer

    return answer

print(solution(p))