# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
def solution(gems):
    result = int(1e9)
    answer = []
    dic = {}
    for s in set(gems) :
        dic[s] = 0


    if len(set(gems)) == 1 :
        return [1,1]

    start,end = 1,2
    gems.insert(0,0)
    for g in gems[start:end]:
        dic[g] += 1

    cnt = 0
    if gems[1] != gems[2] :
        cnt = 2
    else :
        cnt = 1

    dic[gems[end]] += 1

    while end < len(gems) and start < end :
        if cnt == len(set(gems)) :
            if end-start < result :
                answer = [start,end]
                result = end - start
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0 :
                cnt -= 1
            start += 1
        else :
            end += 1
            if end < len(gems) :
                dic[gems[end]] += 1
                if dic[gems[end]] == 1 :
                    cnt += 1

    return answer

print(solution(gems))