k,d = 1,5

def solution(k, d):
    answer = 0
    for i in range(0,d+1,k) :
        max_y = (d**2 - i**2)**(1/2)
        answer += int(max_y // k) + 1
    return answer

print(solution(k,d))