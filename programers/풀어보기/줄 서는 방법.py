n,k = 3,5
from itertools import permutations
from math import factorial
def solution(n, k):
    answer = []
    arr = [i for i in range(1,n+1)]

    for i in range(n,0,-1) :
        fact = factorial(i-1)  # 남은 자리로 만들 수 있는 순열의 개수
        index = (k-1) // fact
        answer.append(arr.pop(index))

        k = (k-1) % fact + 1

    return answer


print(solution(n,k))