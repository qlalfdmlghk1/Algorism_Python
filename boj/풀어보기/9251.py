from collections import defaultdict
a = input()
b = input()
dic = defaultdict()

for i in range(1,len(a)+1) :
    for j in range(len(a)+1-i) :
        word = a[j:j+i]
        dic[word] = True

answer = []

for i in range(1,len(b)+1) :
    for j in range(len(b)+1-i) :
        word = b[j:j+i]
        if word in dic :
            answer.append((len(word),word))

print(answer)

for d in dic :
    if d in b :
        print(d)