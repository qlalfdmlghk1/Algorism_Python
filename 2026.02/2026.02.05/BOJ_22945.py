n = int(input())
members = list(map(int,input().split()))

left,right = 0,n-1
answer = 0

while left < right :
    target = min(members[right], members[left]) * (right-left-1)
    answer = max(answer,target)

    if members[left] <= members[right] :
        left += 1
    else :
        right -= 1

print(answer)
