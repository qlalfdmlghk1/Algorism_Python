# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다.
# 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.
#
# 5457
# 3
# 6 7 8

n = int(input())
m = int(input())
brokens = list(map(int,input().split()))

min_move = abs(100-n)

for num in range(1000001) :
    num = str(num)
    for j in range(len(num)) :
        if int(num[j]) in brokens :
            break
        elif j == len(num)-1 :
            min_move = min(min_move,abs(int(num) - n)+len(num))
print(min_move)