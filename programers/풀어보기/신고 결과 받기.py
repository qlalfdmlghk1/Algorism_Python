id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
check_list = []
dic2 = {}
dic3 = {}
answer = []
for user in id_list :
    check_list.append([user])
report = set(report)  # 한 유저가 같은 유저를 반복 신고한 경우 제거
for lists in report :
    fr,to = lists.split()
    dic2[to] = dic2.get(to,0) + 1
    for i in check_list :
        if fr == i[0] :
            i.append(to)

print(check_list)
print(dic2)
for i in dic2 :
    if dic2[i] >= k :
        dic3[i] = True
print(dic3)
for i in check_list :
    i.pop(0)

for i in check_list :
    cnt = 0
    for j in dic3.keys() :
        if j in i :
            cnt += 1
    answer.append(cnt)
print(answer)