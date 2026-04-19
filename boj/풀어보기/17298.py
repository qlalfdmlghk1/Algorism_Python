n = int(input())
numbers = list(map(int, input().split()))
answer = [-1] * n
stack = [0]

for i in range(n) :
    while stack and numbers[stack[-1]] < numbers[i] : # i번째 인덱스에 있는 값이 아직 오큰 수를 찾지못한 number[인덱스]에 있는 값보다 크다면
        answer[stack.pop()] = numbers[i]  # stack에서 pop으로 빼주기 때문에 다음엔 해당 인덱스를 접근하지 못함
    stack.append(i)  # 아직 오큰 수를 찾지 못한 인덱스를 저장하는 stack
print(*answer)
