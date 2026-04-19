ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

answer = 0
stack = []

for i in ingredient:
    stack.append(i)
    if stack[-4:] == [1, 2, 3, 1]:
        answer += 1
        for k in range(4):
            stack.pop()
print(answer)
