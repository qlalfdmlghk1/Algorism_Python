from collections import deque
order = [5, 4, 3, 2, 1]
n = len(order)
truck = deque()
answer = []

sub = []
idx = 0
num = 0
while idx < n :
    if order[idx] > num :
        num += 1
        sub.append(num)
    elif sub and sub[-1] == order[idx] :
        sub.pop()
        idx += 1
    else :
        print(idx)
print(idx)
