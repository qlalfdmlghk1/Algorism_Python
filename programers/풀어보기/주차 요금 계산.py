# 기본 시간(분) = 180, 기본 요금(원) = 5000, 단위 시간(분) = 10, 단위 요금(원) = 600
fees= [1, 461, 1, 10]
records	= ["00:00 1234 IN"]
# result = [14600, 34400, 5000]
import math
from collections import defaultdict
dic = defaultdict(list)


for car in records :
    dic[car[6:10]].append(int(car[0:2])*60 + int(car[3:5]))

for i in dic.values() :
    if len(i) % 2 == 1 :
        i.append(23*60+59)
# print(dic)

dic = sorted(dic.items(), key=lambda x: x[0])
# print(dic)

times = []
for i in dic :
    total = 0
    while i[1] :
        time1 = i[1].pop()
        time2 = i[1].pop()
        total += time1 - time2
    times.append(total)

answer = []
for i in times :
    if i >= fees[0] :
        answer.append(fees[1] + math.ceil((i - fees[0])/fees[2]) * fees[3])
    else :
        answer.append(fees[1])
print(answer)
