from collections import defaultdict
dic = defaultdict()
a = int(input())
b = int(input())
c = int(input())
num = a * b * c
num = str(num)

for i in range(0,10) :
    dic[str(i)] = 0

for n in num :
    dic[n] += 1

for i in range(0,10) :
    print(dic[str(i)])