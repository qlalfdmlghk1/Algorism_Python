n = int(input())
arr = []

pos_nums = []
neg_nums = []

for _ in range(n) :
    num = int(input())
    if num <= 0 :
        neg_nums.append(num)
    else :
        pos_nums.append(num)

pos_nums.sort(reverse = True)
neg_nums.sort()
pos_len = len(pos_nums)
neg_len = len(neg_nums)

def cul(x,arr) :
    ans = 0
    visited = [False] * (x)
    for i in range(1,x) :
        if not visited[i-1] :
            sec_sum = arr[i-1] + arr[i]
            sec_bind = arr[i-1] * arr[i]
            if sec_bind > sec_sum :
               ans += sec_bind
               visited[i-1] = True
               visited[i] = True
            else :
                ans += arr[i-1]
                visited[i-1] = True
    if x > 0 and not visited[x-1] :
        ans += arr[x-1]
    return ans

print(cul(pos_len,pos_nums) + cul(neg_len,neg_nums))