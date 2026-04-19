msg = 'KAKAO'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic = {}
answer = []
for index,i in enumerate(alpha) :
    dic[i] = index+1

w = c = 0
new_index = 27

while True :
    c += 1
    if c == len(msg) :
        answer.append(dic[msg[w:c]])
        break

    if msg[w:c+1] not in dic :
        dic[msg[w:c + 1]] = new_index
        new_index += 1
        answer.append(dic[msg[w:c]])
        w = c

print(answer)