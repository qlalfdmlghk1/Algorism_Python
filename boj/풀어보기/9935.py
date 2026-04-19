total = input()
s = input()
stack = []

for t in total :
    stack.append(t)
    if stack[len(stack)-len(s):] == list(s) :
        for _ in range(len(s)) :
            stack.pop(-1)

if stack :
    print(*stack, sep = '')
else :
    print("FRULA")