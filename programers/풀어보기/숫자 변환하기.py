x,y,n = 10,40,5

answer = 0
dp = set()
dp.add(x)

while dp :
    if y in dp :
        print(answer)
        break
    else :
        dp_y = set()
        for i in dp :
            if i+n <= y :
                dp_y.add(i+n)
            if i*2 <= y :
                dp_y.add(i*2)
            if i*3 <= y :
                dp_y.add(i+3)
        dp = dp_y
        answer += 1
print(-1)