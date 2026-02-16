T = int(input())


for _ in range(T) :
    N,M = map(int,input().split())
    cnt = 0
    arr = list(map(int, input().split()))
    arr2 = []
    for index,a in enumerate(arr) :
        arr2.append((a,index))
    
    while arr2 :
        # print(arr2)
        num = arr.pop(0)
        target = arr2.pop(0)
        if len(arr2) == 0 :
            print(N)
            break

        else :    
            if target[0] >= max(arr) :    
                cnt += 1
                if target[1] == M :
                    print(cnt)
                    break
            else :
                arr2.append(target)
                arr.append(num)