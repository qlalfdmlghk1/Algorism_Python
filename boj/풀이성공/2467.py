n = int(input())
solution = list(map(int,input().split()))

solution.sort()

left = 0
right = n-1
result = int(1e11)
answer = []

while left < right :
    diff = solution[left] + solution[right]
    cur = abs(diff)
    if result >= cur:
        answer.append([solution[left], solution[right]])
        result = cur

    if diff < 0 :
        left += 1
    else :
        right -= 1

print(answer[-1][0],answer[-1][1])
