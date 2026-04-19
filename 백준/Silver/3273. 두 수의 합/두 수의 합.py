N = int(input())
NUMS = list(map(int,input().split()))
K = int(input())

NUMS.sort()
left,right = 0,N-1

answer = 0
while left < right :
    temp = NUMS[left] + NUMS[right]
    if temp == K :
        answer += 1
        left += 1
    elif temp < K :
        left += 1
    else :
        right -= 1
print(answer)