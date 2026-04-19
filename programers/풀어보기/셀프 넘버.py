# 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
dp = {}
sum = 0
for num in range(1,10001) :
    sum = num
    num = str(num)
    for i in num :
        sum += int(i)
    dp[sum] = True

for i in range(1,10001) :
    if i not in dp :
        print(i)
