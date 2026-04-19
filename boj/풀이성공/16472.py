n = int(input())
word = input().strip()
dic = {}

start = 0
end = 1
dic[word[start]] = 1
if word[end] in dic :
    dic[word[end]] += 1
else :
    dic[word[end]] = 1

result = n
while end < len(word) :
    if len(dic) <= n :
        result = max(result, end-start+1)
        end += 1
        if end == len(word) :
            break
        if word[end] in dic :
            dic[word[end]] += 1
        else :
            dic[word[end]] = 1
    else :
        if dic[word[start]] > 1 :
            dic[word[start]] -= 1
        elif dic[word[start]] == 1 :
            dic.pop(word[start])
        start += 1
print(result)