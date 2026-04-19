n = int(input())  # 앵무새 수 (1~100)

arr = []

for _ in range(n) :
    arr.append(input().split())  # 단어 수 (1~100) / 각 단어 (1~32)

cseteram = list(input().split())

flag = True

for cur in cseteram :
    flag = False
    for a in arr :
        if a and a[0] == cur :
            a.pop(0)
            flag = True
            break
        else :
            continue
    if flag :
        continue
    else :
        print("Impossible")
        exit()


for a in arr :
    if a :
        flag = False
        print("Impossible")
        exit()

if flag :
    print("Possible")