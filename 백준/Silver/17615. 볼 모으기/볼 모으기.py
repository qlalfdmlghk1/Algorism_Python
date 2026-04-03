N = int(input())
balls = list(map(str,input()))
red,blue = 0,0

for ball in balls :
    if ball == "R" : red += 1
    else : blue += 1

# 빨간공 선택한 경우
case1 = 0
if balls[0] == "R" :
    for ball in balls :
        if ball == "R" :
            case1 += 1
        else :
            break
case1 = red - case1

case2 = 0
if balls[-1] == "R" :
    for ball in balls[::-1] :
        if ball == "R" :
            case2 += 1
        else :
            break
case2 = red - case2


case3 = 0
if balls[0] == "B" :
    for ball in balls :
        if ball == "B" :
            case3 += 1
        else :
            break
case3 = blue - case3

case4 = 0
if balls[-1] == "B" :
    for ball in balls[::-1] :
        if ball == "B" :
            case4 += 1
        else :
            break
case4 = blue - case4

# print(case1,case2,case3,case4)
print(min(case1,case2,case3,case4))