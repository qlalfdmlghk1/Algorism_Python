N = int(input())
liquid = list(map(int,input().split()))
liquid.sort()

left,right = 0,N-1
temp = 2_000_000_001
ans = []

while left < right :
    a,b = liquid[left],liquid[right]
    if temp >= abs(a+b) :
        temp = abs(a+b)
        ans = [a,b]

    if a+b > 0 :
        right -= 1
    else :
        left += 1
        

print(*ans)