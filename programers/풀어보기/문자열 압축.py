s = "abcabcdede"
s_len = len(s)
answer = 1e9
for size in range(1,len(s)//2+1) :
    stack = []
    sentence = ''
    words = [s[i:i+size] for i in range(0,s_len,size)]
    stack.append([words[0],1])
    for j in words[1:] :
        if stack[-1][0] == j :
            temp,cnt = stack.pop()
            stack.append([temp,cnt+1])
        else :
            stack.append([j,1])
    for temp_2,cnt_2 in stack :
        if cnt_2 == 1 :
            sentence += temp_2
        else :
            sentence += (temp_2 + str(cnt_2))
    # print(sentence)
    answer = min(len(sentence),answer)
print(answer)