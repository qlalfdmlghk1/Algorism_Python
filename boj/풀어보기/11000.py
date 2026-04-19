from heapq import heappush,heappop

n = int(input())
times = []
pq = []

for _ in range(n) :
    s,t = map(int, input().split())
    times.append((s,t))
times.sort()

pq.append((times[0][1]))  # 가장 빨리 끝나는 시간
for i in range(1,n) :
    if pq[0] <= times[i][0] :
        heappop(pq)
    heappush(pq,times[i][1])

print(len(pq))