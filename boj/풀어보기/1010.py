# Solution 1
# t = int(input())
# for _ in range(t) :
#     answer = 1
#     n,m = map(int,input().split())

#     for i in range(n) :
#         answer *= (m-i)
#         answer /= (i+1)
#     print(int(answer))

# Solution 2
# from math import factorial
# t = int(input())
# for _ in range(t) :
#     n,m = map(int,input().split())
#     print(factorial(m) // (factorial(n) * factorial(m-n)))


# Solution 3
t = int(input())
dp = [[1] * 31 for _ in range(31)]
for i in range(1,31) :
    for j in range(1,i) :
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for _ in range(t) :
    n,m = map(int,input().split())
    print(dp[m][n])