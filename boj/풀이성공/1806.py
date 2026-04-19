n,s = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(1,n) :
    arr[i] = arr[i-1] + arr[i]
arr.insert(0,0)

left = 0
right = 1
answer = 1e9

while left <= right and right <= n:
    if arr[right] - arr[left] >= s :
        answer = min(right - left, answer)
        left += 1
    else :
        right += 1

if answer < 1e9 :
    print(answer)
else :
    print(0)