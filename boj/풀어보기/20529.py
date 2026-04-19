from itertools import combinations
t = int(input())

for _ in range(t) :
    cnt = 0
    mini = 21470000
    n = int(input())
    arr = list(map(str, input().split()))
    if n > 32 :
        print(0)
        continue
    for mbti in combinations(arr,3) :
        cnt = 0
        for i in range(2) :
            for j in range(1, 3):
                if mbti[i][0] != mbti[j][0] :
                    cnt += 1
                if mbti[i][1] != mbti[j][1] :
                    cnt += 1
                if mbti[i][2] != mbti[j][2] :
                    cnt += 1
                if mbti[i][3] != mbti[j][3] :
                    cnt += 1
        mini = min(mini, cnt)

    print(cnt)