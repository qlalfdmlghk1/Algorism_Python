def solution(s) :
    answer = 0
    for i in range(len(s)) :
        word_list = list(s)
        word_list = word_list[i:len(s)] + word_list[:i]

        stack = []

        while word_list :
            cur = word_list.pop(0)
            if not stack :
                stack.append(cur)
            else :
                if cur not in [')',']','}'] :
                    stack.append(cur)
                else :
                    if cur == ')' and stack[-1] == '(' :
                        stack.pop()
                    elif cur == ']' and stack[-1] == '[' :
                        stack.pop()
                    elif cur == '}' and stack[-1] == '{' :
                        stack.pop()
                    else :
                        stack.append(cur)
        if not stack :
            answer += 1
    return answer