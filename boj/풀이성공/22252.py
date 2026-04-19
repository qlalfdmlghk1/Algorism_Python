import sys, heapq
input = sys.stdin.readline
q = int(input())
dic = {}
answer = 0
for _ in range(q) :
    li = list(input().split())
    num = li[0]
    idx = li[1]  # 고릴라 이름
    k_idx = int(li[2])
    if num == "1" :
        infos = list(int(i) for i in li[3:])
        if idx not in dic :
            dic[idx] = []
        for info in infos :
            dic[idx].append(info)
        dic[idx].sort(reverse=True)

    elif num == "2" :
        if idx in dic and dic[idx] :
            answer += sum(dic[idx][0:k_idx])
            dic[idx] = dic[idx][k_idx:]

print(answer)
