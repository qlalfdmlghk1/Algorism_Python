from heapq import heappush,heappop
pq = []
schedule = [False] * 1001

n = int(input())
scores = []
for _ in range(n) :
    d,w = map(int,input().split())
    heappush(pq,(-w,d))

result = 0
while pq :
    score,day = heappop(pq)
    for i in range(day,0,-1) :
        if not schedule[i] :
            schedule[i] = score
            result += -score
            break
print(result)