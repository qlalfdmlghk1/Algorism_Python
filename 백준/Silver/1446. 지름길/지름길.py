N,D = map(int,input().split())
distance = [i for i in range(D+1)]

short_route = []
for _ in range(N) :
    start,end,length = map(int,input().split())
    if 0 <= start <= D and 0 <= end <= D :
        short_route.append((start,end,length))
short_route.sort()

for i in range(0,D+1) : 
    distance[i] = min(distance[i],distance[i-1] + 1)
    while short_route and short_route[0][0] == i :
        a,b,c = short_route.pop(0)
        distance[b] = min(distance[b],distance[i] + c)

print(distance[D])