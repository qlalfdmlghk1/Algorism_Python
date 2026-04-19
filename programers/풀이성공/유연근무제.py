schedules,startday = [730, 855, 700, 720],1
timelogs = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]

def solution(schedules, timelogs, startday):
    end_times = []
    for schedule in schedules :
        if (schedule + 10) % 100 >= 60 :
            end_time = schedule + 100 - 60
        else :
            end_time = schedule
        end_times.append(end_time + 10)

    answer = len(timelogs)
    for idx,timelog in enumerate(timelogs) :  # idx : n번째 사람
        # print(idx+1, "번째 사람")
        day_num = startday % 7
        for t in timelog:
            # print(end_times[idx], t)

            if 0 < day_num < 6 and end_times[idx] < t :
                answer -= 1
                break
            day_num += 1
            day_num = day_num % 7
            # print("요일", day_num)
    return answer

print(solution(schedules,timelogs,startday))