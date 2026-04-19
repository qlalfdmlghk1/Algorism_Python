from heapq import heappush,heappop,heapify
n = int(input())
pq = []

for _ in range(n) :
    num = int(input())
    heappush(pq,num)

answer = 0
while len(pq) > 1 :
    # print(pq)
    card1 = heappop(pq)
    card2 = heappop(pq)
    card = card1 + card2
    answer += card
    heappush(pq,card)
print(answer)