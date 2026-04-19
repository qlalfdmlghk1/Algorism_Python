# 세 개의 기둥
# 1. 한 번에 하나의 원판만 옮길 수 있습니다.
# 2. 큰 원판이 작은 원판 위에 있어서는 안됩니다.
# 3. 1번 기둥에 n개의 원판이 있고, 이 n개의 원판을 3번 원판으로 최소 횟수로 옮기려고 합니다.
#
# 1번 기둥에 있는 원판의 개수 n이 매개변수로 주어질 때, n개의 원판을 3번 원판으로 최소로 옮기는 방법을 return.
#
# n,result = 2, [ [1,2], [1,3], [2,3] ]
answer = []
n = 2
def hanoi(n,start,end,mid) :
    if n == 1 :
        answer.append([start,end])
        return
    else :
        hanoi(n-1, start,mid,end)
        answer.append([start,end])
        hanoi(n-1, mid,end,start)

hanoi(n,1,3,2)
print(answer)