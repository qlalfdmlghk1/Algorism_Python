import heapq
T = int(input())
for t in range(T) :
    k = int(input())
    pq = []
    heapq.heapify(pq)
    arr = list(map(int,input().split()))
    for a in arr :
       heapq.heappush(pq,a)

    result = 0
    while len(pq) > 1 :
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        result += (a+b)
        heapq.heappush(pq,a+b)
    print(result)


