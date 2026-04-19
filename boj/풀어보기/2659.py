from collections import defaultdict
nums = list(map(str, input().split()))
str_num = nums[0] + nums[1] + nums[2] + nums[3]

def check_clock_num(num) :  # 십자가의 4개 수 주어졌을 때, 거기에서의 시계수
    min = int(num)
    for i in range(1, 4):
        tmp = int(''.join(map(str, num[i:] + num[:i])))
        if min > tmp:
            min = tmp
    return min

cnt = 1
clock_nums = defaultdict()
target_num = check_clock_num(str_num)

for i in range(1111,target_num) :
    if '0' not in str(i) and check_clock_num(str(i)) == i :
        cnt += 1
print(cnt)