stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3

def solution(stones, k):
    left = 0
    right = len(stones)
    while left <= right :
        mid = (left + right) // 2
        result = 0
        flag = True
        for stone in stones :
            if stone < mid :
                result += 1
            else :
                result = 0
                


    return answer

print(solution(stones,k))