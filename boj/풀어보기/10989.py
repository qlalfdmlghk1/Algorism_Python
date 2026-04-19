import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
numbers = list(defaultdict())
for _ in range(n) :
    num = int(input())
    print(numbers[num])
    # if not numbers[num] :
    #     numbers[num] = 0
    # else :
    #     numbers[num] += 1
numbers.sort()
print(numbers)