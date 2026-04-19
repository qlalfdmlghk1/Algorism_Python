import heapq
n = int(input())
people = []  # 사람들
using = []   # 쓰고 있는 컴퓨터
available = []  # 사용 가능한 컴퓨터
count = []   # 컴퓨터 사용 횟수

for _ in range(n) :
    start_time, end_time = map(int, input().split())
    people.append([start_time,end_time])
people.sort()

for a,b in people :  # 시작 시간 빠른 순으로
    # 1. 끝난 컴퓨터 다시 세팅해주기
    while using and using[0][0] <= a :
        idx,com_idx = heapq.heappop(using)
        heapq.heappush(available,com_idx)

    # 2. 사용할 컴퓨터 정하기
    if available :
        com_idx = heapq.heappop(available)
        count[com_idx] += 1
    else :
        com_idx = len(count)
        count.append(1)

    # 3.
    heapq.heappush(using,(b,com_idx))

print(len(count))
for i in count :
    print(i,end=" ")