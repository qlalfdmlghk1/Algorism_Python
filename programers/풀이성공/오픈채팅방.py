record = ["Enter uid1234 Muzi","Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer,result = [],[]
    dic = {}
    # 딕셔너리 : 키 - ID / 값 - 아이디
    # 리스트 돌면서 '키' 로 저장해놓고 한 번에 값으로 바꾸기
    for r in record:
        arr = list(r.split())
        if arr[0] == "Enter" :
            answer.append(arr[1] + " 님이 들어왔습니다.")
            dic[arr[1]] = arr[2]
        elif arr[0] == "Leave" :
            answer.append(arr[1] + " 님이 나갔습니다.")
        else :
            dic[arr[1]] = arr[2]

    for ans in answer :
        a,b,c = list(ans.split())
        if a in dic :
            result.append(dic[a] + b + " " + c)
    return result

print(solution(record))
