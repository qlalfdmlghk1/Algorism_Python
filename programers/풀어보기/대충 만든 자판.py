keymap, targets	= ["BC"], ["AC", "BC"]
answer = 0
result = []
dic = {}
for key in keymap :
    for index,i in enumerate(key) :
        if i in dic :
            dic[i] = min(dic[i], index+1)
        else :
            dic[i] = index+1
for target in targets :
        for i in target :
            if i not in dic :
                answer = -1
                break
            else :
                answer += dic[i]
        result.append(answer)
        answer = 0
print(result)