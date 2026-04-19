numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"

def solution(numbers, hand) :
    result = ''
    pre_left = [(0,0)]
    pre_right = [(2,0)]

    def check_center(target) :
        dis_left = abs(target[0] - pre_left[-1][0]) + abs(target[1] - pre_left[-1][1])
        dis_right = abs(target[0] - pre_right[-1][0]) + abs(target[1] - pre_right[-1][1])
        if dis_left > dis_right:
            pre_right.append((target[0], target[1]))
            return 'R'
        elif dis_left < dis_right:
            pre_left.append((target[0], target[1]))
            return 'L'
        else:
            if hand == "left":
                pre_left.append((target[0], target[1]))
                return 'L'
            else:
                pre_right.append((target[0], target[1]))
                return 'R'

    for num in numbers :
        if num == 1 or num == 4 or num == 7 :
            result += 'L'
            if num == 1 : pre_left.append((0,3))
            if num == 4 : pre_left.append((0,2))
            if num == 7 : pre_left.append((0,1))
        elif num == 3 or num == 6 or num == 9 :
            result += 'R'
            if num == 3 : pre_right.append((2,3))
            if num == 6 : pre_right.append((2,2))
            if num == 9 : pre_right.append((2,1))
        else :
            if num == 2 :
                result += check_center([1,3])
            elif num == 5 :
                result += check_center([1,2])
            elif num == 8 :
                result += check_center([1,1])
            elif num == 0 :
                result += check_center([1,0])

    return result

print(solution(numbers, hand))
