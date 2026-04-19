n = int(input())
words = []
alpha = [0] * 26

for _ in range(n) :
    s = input()
    words.append(s)

for word in words :
    for idx,w in enumerate(word) :
        alpha[ord(w)-65] += 10**(len(word)-idx-1)

alpha.sort(reverse=True)

num = 9
answer = 0
for a in alpha :
    if a != 0 :
        answer += (num * a)
    num -= 1
print(answer)