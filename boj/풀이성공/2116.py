import sys
sys.setrecursionlimit(10**6)

n = int(input())
dices = []
for _ in range(n) :
    dices.append(list(map(int,input().split())))

answer = []
# 양면 짝 : A-F, B-D, C-E
def check_dice(dice_num,upper_num,result) :
    global answer
    if dice_num == n :
        answer.append(result)
        return True

    else :
        idx = dices[dice_num].index(upper_num)
        if idx == 0 :
            nex_upper_num = dices[dice_num][5]
            result += max(dices[dice_num][1:5])
            check_dice(dice_num+1, nex_upper_num,result)
            return True
        elif idx == 1 :
            nex_upper_num = dices[dice_num][3]
            result += max(dices[dice_num][0],dices[dice_num][2],dices[dice_num][4],dices[dice_num][5])
            check_dice(dice_num + 1, nex_upper_num,result)
            return True
        elif idx == 2 :
            nex_upper_num = dices[dice_num][4]
            result += max(dices[dice_num][0],dices[dice_num][1],dices[dice_num][3],dices[dice_num][5])
            check_dice(dice_num + 1, nex_upper_num,result)
            return True
        elif idx == 3 :
            nex_upper_num = dices[dice_num][1]
            result += max(dices[dice_num][0],dices[dice_num][2],dices[dice_num][4],dices[dice_num][5])
            check_dice(dice_num + 1, nex_upper_num,result)
            return True
        elif idx == 4 :
            nex_upper_num = dices[dice_num][2]
            result += max(dices[dice_num][0],dices[dice_num][1],dices[dice_num][3],dices[dice_num][5])
            check_dice(dice_num + 1, nex_upper_num,result)
            return True
        elif idx == 5 :
            nex_upper_num = dices[dice_num][0]
            result += max(dices[dice_num][1:5])
            check_dice(dice_num + 1, nex_upper_num,result)
            return True

for i in range(1,7) :
    check_dice(0,i,0)
print(max(answer))