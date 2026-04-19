n = int(input())  # 과제 개수
homework = []

for i in range(n) :
    d,t = map(int,input().split())  # d일이 걸림, t일 안에 끝내야 함 (오늘은 0일)
    homework.append((d,t))

homework.sort(key = lambda x : x[1], reverse = True)

time = homework[0][1]

for hw in homework :
    duration = hw[0]
    end = hw[1]
    if time >= end :
        time = end - duration
    else :
        time = time - duration
print(time)