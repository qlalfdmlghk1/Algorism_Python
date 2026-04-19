import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0
for i in range(n-2) :
    left = i+1
    right = n-1
    target = -arr[i]

    while left < right :
        s = arr[left] + arr[right]
        if target == s :
            if arr[left] == arr[right] :
                cnt += (right-left) * (right-left+1) // 2
                break
            else :
                l_cnt = 1
                r_cnt = 1
                while left + 1 < right and arr[left] == arr[left+1] :
                    l_cnt += 1
                    left += 1
                while right - 1 > left and arr[right] == arr[right-1] :
                    r_cnt += 1
                    right -= 1
                cnt += l_cnt * r_cnt
                left += 1
                right -= 1

        elif s < target :
            left += 1
        else :
            right -= 1

print(cnt)