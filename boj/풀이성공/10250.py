t = int(input())
for _ in range(t) :
    h,w,n = map(int,input().split())
    x = n // h + 1
    y = n % h

    if y == 0 :
        y = h
        x -= 1

    if x < 10 :
        x = '0' + str(x)


    print(str(y) + str(x))