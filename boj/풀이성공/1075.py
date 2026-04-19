n = int(input())
k = int(input())
num = n // 100 * 100
for i in range(0,100) :
    new_num = num + i
    if new_num % k == 0 :
        if i < 10 :
            print('0'+str(i))
            break
        else :
            print(i)
            break