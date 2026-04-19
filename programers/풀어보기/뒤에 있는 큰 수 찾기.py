numbers = [9, 1, 5, 3, 6, 2]	# result = [3, 5, 5, -1]
# [2, 3, 3, 5]	[-1, 5, 6, 6, -1, -1]
stack = []
answer = [-1] * len(numbers)
for ind,num in enumerate(numbers) :
    while stack and numbers[stack[-1]] < num :
        answer[stack.pop()] = num
    stack.append(ind)
print(answer)