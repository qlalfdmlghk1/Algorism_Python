h,m = map(int,input().split())

fake_time = h * 60 + m
real_time = fake_time - 45

if real_time < 0 :
    print(23, 60+real_time)
else :
    print(real_time//60, real_time%60)