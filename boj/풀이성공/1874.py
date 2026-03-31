n = int(input())
stack = []
answer = []
push_num = 1
for _ in range(n) :
    target = int(input())
    while not stack or stack[-1] < target :
        stack.append(push_num)
        push_num += 1
        answer.append('+')

    if stack[-1] == target :
        answer.append('-')
        stack.pop()

if stack :
    print("NO")
else :
    print(*answer, sep="\n")


