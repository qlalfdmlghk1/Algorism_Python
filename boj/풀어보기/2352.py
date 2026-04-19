import bisect

n = int(input())
port = list(map(int,input().split()))

result = [port[0]]

for x in range(1,n) :
    if port[x] > result[-1] :
        result.append(port[x])
    else :
        index = bisect.bisect_left(result,port[x])
        result[index] = port[x]
print(len(result))