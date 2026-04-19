# n = int(input())
# cnt = 0
# for i in range(1,n) :
#     if (i % 2 == 1) :
#         print(type(n/int(i)))
#         print(isinstance(n/i, int))
#         if (isinstance(n/i, int) and ((n//i - (i-1//2)) >= 1)) :
#             cnt += 1
#             print(i)
#     else :
#         if (((n//i + n//i+1)*(i//2) == n) and((n//i - (i-1//2)) >= 1)) :
#             cnt += 1
#             print(i)
# print(cnt)

n = int(input())
cnt, sum = 0, 3
lp, rp = 1,2

while lp <= rp :
    if sum < n :
        rp += 1
        sum += rp
    elif sum > n :
        sum -= lp
        lp += 1
    else :
        cnt += 1
        rp += 1
        sum += rp
print(cnt)
