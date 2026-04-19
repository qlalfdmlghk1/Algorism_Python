from collections import defaultdict

s = input()
n = len(s)
dic = defaultdict(list)

for i in range(1,n+1) :
    for k in range(0,n-i+1) :
        dic[s[k:k+i]] = True
print(len(dic))


