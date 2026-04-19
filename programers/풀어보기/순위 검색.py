info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    candidate = []
    standard = []
    # 지원자 리스트 정리
    for i in info :
        candidate.append(i.split())

    # 조건 정리
    for q in query :
        q = q.replace(" and "," ")
        standard.append(q.split())

    # 조건에 만족하는가?
    def check(person,check_point) :
        for i in range(5) :
            if i < 4 :
                if check_point[i] == "-" :
                    continue
                else :
                    if person[i] != check_point[i] :
                        return 0
            else :
                if int(person[i]) >= int(check_point[i]) :
                    return 1
                else :
                    return 0


    for s in standard :
        result = 0
        for c in candidate :
            result += check(c,s)
        answer.append(result)
    return answer

print(solution(info,query))