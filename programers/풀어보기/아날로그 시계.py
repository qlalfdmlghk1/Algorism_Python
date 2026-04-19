h1,m1,s1,h2,m2,s2 = 12,0,0,12,0,30  # h1시 m1분 s1초부터 h2시 m2분 s2초까지 알람이 울리는 횟수

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2

    if start_time == 0 or start_time == 60 * 60 * 12:
        answer += 1

    for time in range(start_time,end_time) :
        cur_s = time * 6 % 360
        cur_m = time / 10 % 360
        cur_h = time / 120 % 360

        nex_s = (time+1) * 6 % 360
        nex_m = (time+1) / 10 % 360
        nex_h = (time+1) / 120 % 360

        if int(nex_s) == 0 : nex_s = 360
        if int(nex_m) == 0 : nex_m = 360
        if int(nex_h) == 0 : nex_h = 360

        if cur_h < cur_s and nex_h >= nex_s :
            answer += 1
        if cur_m < cur_s and nex_m >= nex_s :
            answer += 1
        if cur_h < cur_s and nex_h >= nex_s and cur_m < cur_s and nex_m >= nex_s :
            answer -= 1
    return answer

print(solution(h1, m1, s1, h2, m2, s2))