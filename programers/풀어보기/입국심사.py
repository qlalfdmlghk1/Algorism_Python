n,times = 6,[7,10] # n명의 사람, 심사하는데 걸리는 시간

def solution(n, times):
    answer = 0
    left, right = 0,max(times) * n
    while left <= right :
        mid = (left + right) // 2
        people = 0
        for time in times :
            people += mid // time
            if people > n : # 시간이 너무 적다는 것
                break
        if people >= n : # 시간이 너무 적다는 것
            answer = mid
            right = mid - 1
        else : # 시간이 너무 길다
            left = mid + 1
    return answer


print(solution(n,times))