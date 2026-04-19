from heapq import heappush, heappop, heapify

t = int(input())
for _ in range(t) :
    k = int(input())
    files = list(map(int,input().split()))
    pq = []
    heapify(pq)
    result = 0
    for file in files :
        heappush(pq,file)
    while len(pq) > 1 :
        a1 = heappop(pq)
        a2 = heappop(pq)
        result += (a1+a2)
        heappush(pq, (a1+a2))
        print(pq)
    print(result)