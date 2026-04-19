X = "5525"
Y = "1255"
answer = []
for i in (set(X) & set(Y)) :
    for j in range(min(X.count(i),Y.count(i))) :
        answer.append(i)

answer.sort(reverse = True)

if len(answer) == 0 :
    print("-1")
else :
    answer = int(''.join(answer))
    print(str(answer))
