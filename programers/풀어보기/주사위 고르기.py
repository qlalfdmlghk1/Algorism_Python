dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]

from itertools import combinations

n = len(dice)

total = 0
for d in dice :
    total += sum(d)

result = []
is_max = 0
for i in combinations(dice,n//2) :
    a = 0
    cur = []
    for j in range(n//2) :
        a += sum(i[j])
        cur.append(dice.index(i[j])+1)
    # print(cur)
    # print(a)
    if is_max <= a :
        is_max = a
        result = cur

print(result)
