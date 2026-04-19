# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리
# 평균이 얼마가 되는지 return
jobs = [[0, 3], [1, 9], [2, 6]]
import heapq

current_time,finished_job,using_time, current_job = 0,0,0,0
aver = 0
pq = []

jobs.sort()  # 첫번째 요소를 기준으로 정렬

while finished_job < len(jobs) :
    while current_job < len(jobs) and current_time >= jobs[current_job][0]  :
        start, duration = jobs[current_job]
        heapq.heappush(pq, (duration, start))
        current_job += 1
        print(pq)
        print(current_job)

    if pq :
        duration, start = heapq.heappop(pq)
        current_time += duration
        using_time = current_time - start
        aver += using_time
        finished_job += 1

    else:
        current_time = jobs[current_job][0]

print(aver//len(jobs))


