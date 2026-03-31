n = int(input())
m = int(input())
arr = list(map(int,input().split()))
arr.sort()

left = 0
right = n-1
answer = 0

while left < right :
    # mid = (left + right) // 2
    check = arr[left] + arr[right]
    if check == m :
        answer += 1
        right -= 1
    elif check < m :
        left += 1
    else :
        right -= 1
print(answer)