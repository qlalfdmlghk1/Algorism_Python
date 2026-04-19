# 55-50+40
answer = []
nums = list(input().split('-'))
for i in nums :
    mid_sum = 0
    k = list(map(int,i.split('+')))
    answer.append(sum(k))
result = answer[0]
for i in answer[1:] :
    result -= i
print(result)
