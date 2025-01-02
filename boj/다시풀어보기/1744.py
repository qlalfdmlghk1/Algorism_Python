n = int(input())
arr = []
visited = [False] * (n)
for _ in range(n) :
    arr.append(int(input()))

arr.sort(reverse = True)

sum = 0
for i in range(1,n) :
    if not visited[i-1] :
        sec_sum = arr[i-1] + arr[i]
        sec_bind = arr[i-1] * arr[i]
        if sec_bind > sec_sum :
           sum += sec_bind
           visited[i-1] = True
           visited[i] = True
        else :
            sum += arr[i-1]
            visited[i-1] = True
    print(visited)
    print(sum)

if not visited[n-1] :
    sum += arr[i-1]
print(sum)