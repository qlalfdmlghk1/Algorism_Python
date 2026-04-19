from collections import Counter
topping	= [1, 2, 1, 3, 1, 4, 1, 2]
answer = 0

dic1 = Counter(topping)
dic2 = {}

for i in range(len(topping)) :
    if topping[i] in dic2 :
        dic2[topping[i]] += 1
    else :
        dic2[topping[i]] = 1
    dic1[topping[i]] -= 1

    if dic1[topping[i]] == 0 :
        dic1.pop(topping[i])

    if len(dic1) == len(dic2) :
        answer += 1

print(answer)