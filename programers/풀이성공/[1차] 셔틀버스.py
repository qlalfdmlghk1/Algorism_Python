n,t,m,timetable =	10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
# n: 셔틀 운행 횟수, t: 셔틀 운행 간격, m: 한 셔틀에 탈 수 있는 최대 크루 수, timetable: 크루가 대기열에 도착하는 시각 배열

def solution(n, t, m, timetable):
    answer = 0
    crews = []

    # timetable 의 정수화
    for tt in timetable :
        hour,minuate = tt.split(":")
        time = int(hour) * 60 + int(minuate)
        crews.append(time)
    crews.sort()
    crew_cnt = len(crews)

    buses = []  # 버스 오는 시간
    for i in range(n) :
        buses.append(540 + t * i)
    bus_cnt = len(buses)

    def change_time(x) :
        hour = x // 60
        minuate = x % 60
        if hour < 10 :
            hour = "0" + str(hour)
        if minuate < 10:
            minuate = "0" + str(minuate)
        time = str(hour) + ":" + str(minuate)
        return time

    crew_idx = 0
    for bus_idx,bus in enumerate(buses) :
        cnt = 0  # 지금 버스에 몇 명이 탔냐?

        while crew_idx < crew_cnt and crews[crew_idx] <= bus and cnt < m :
            crew_idx += 1
            cnt += 1

        # 마지막 버스인 경우 판단
        if bus_idx + 1 == bus_cnt :
            # 만석일 경우 -> 마지막 사람보다 1분 먼저
            if cnt >= m :
                answer = crews[crew_idx-1] - 1
            # 만석이 아닐 경우 -> 버스 도착 시간
            else :
                answer = bus
    return change_time(answer)

print(solution(n,t,m,timetable))