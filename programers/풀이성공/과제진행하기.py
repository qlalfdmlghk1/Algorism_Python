plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]] # 과제명, 시작 시간, 걸린 시간
def solution(plans):
    for plan in plans :
        h,m = plan[1].split(":")
        plan[1] = int(h) * 60 + int(m)
        plan[2] = int(plan[2])

    plans.sort(key = lambda x : x[1])

    yet = []
    answer = []

    for i in range(len(plans)-1) :
        # print("yet : ",yet)
        if plans[i][1] + plans[i][2] <= plans[i+1][1] :
            answer.append(plans[i][0])
            extra_time = plans[i+1][1] - (plans[i][1] + plans[i][2])
            # print("extra_time : " + str(extra_time))
            while yet and extra_time :
                if yet[-1][2] <= extra_time :
                    extra_time -= yet[-1][2]
                    answer.append(yet.pop(-1)[0])
                else :
                    yet[-1][2] -= extra_time
                    extra_time = 0

        else :
            plans[i][2] -= (plans[i+1][1] - plans[i][1])
            yet.append(plans[i])

    answer.append(plans[-1][0])

    while yet :
        answer.append(yet.pop(-1)[0])
    return answer

print(solution(plans))