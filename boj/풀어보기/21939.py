import heapq, sys
from collections import defaultdict

input = sys.stdin.readline
min_pq = []
max_pq = []
heapq.heapify(min_pq)
heapq.heapify(max_pq)
removed_problem = defaultdict(bool)

n = int(input())
for _ in range(n) :
    p, l = map(int,input().split())  # 문제 번호, 난이도
    heapq.heappush(min_pq,(l,p))
    heapq.heappush(max_pq,(-l,-p))

m = int(input())
for _ in range(m) :
    arr = input().split()

    if arr[0] == "recommend" :
        if arr[1] == "1" :  # 가장 어려운 문제의 번호를 출력
            while max_pq:
                difficulty, problem = max_pq[0]  # 최상위 요소 확인 (삭제 X)
                problem = -problem  # 원래 번호로 변환
                if not removed_problem[problem]:  # 삭제되지 않은 경우 출력
                    print(problem)
                    break
                heapq.heappop(max_pq)  # 삭제된 문제라면 제거하고 다시 확인

        elif arr[1] == "-1" :  # 가장 쉬운 문제의 번호를 출력
            while min_pq:
                difficulty, problem = min_pq[0]   # 최상위 요소 확인 (삭제 X)
                if not removed_problem[problem]:  # 삭제되지 않은 경우 출력
                    print(problem)
                    break
                heapq.heappop(min_pq)  # 삭제된 문제라면 제거하고 다시 확인

    elif arr[0] == "add" :
        heapq.heappush(min_pq,(int(arr[2]),int(arr[1])))
        heapq.heappush(max_pq, (-int(arr[2]),-int(arr[1])))
        removed_problem[int(arr[1])] = False

    elif arr[0] == "solved" :
        num = int(arr[1])
        removed_problem[num] = True

        # 삭제된 문제를 힙에서 즉시 제거
        while min_pq and removed_problem[min_pq[0][1]]:
            heapq.heappop(min_pq)
        while max_pq and removed_problem[-max_pq[0][1]]:
            heapq.heappop(max_pq)
