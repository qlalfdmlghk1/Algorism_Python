while True :
    s = input()
    stack = []
    if s == '.' :
        break
    else :
        for word in s :
            if word == '(' or word == '[' :
                stack.append(word)
            elif word == ')' :
                if stack and stack[-1] == '(' :
                    stack.pop()
                else :
                    stack.append(word)
            elif word == ']' :
                if stack and stack[-1] == '[' :
                    stack.pop()
                else :
                    stack.append(word)
            else :
                continue
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
