N,number = 5,12
def solution(N, number):
    answer = 0
    dp = [set([int(str(N)*i)]) for i in range(1,9)]
    for i in range(8) :
        for j in range(i) :
            for num1 in dp[j] :
                for num2 in dp[i-j-1] :
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0 :
                        dp[i].add(num1 // num2)
        print(dp)
        if number in dp[i] :
             return i+1
    return -1
print(solution(N,number))