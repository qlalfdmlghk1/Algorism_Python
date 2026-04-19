msg = "TOBEORNOTTOBEORTOBEORNOT"
dic = {chr(i + 64): i for i in range(1, 27)}
cur, nex = 0, 0  # 현재 인덱스, 다음 인덱스
answer = []
idx = 26

while True :
    nex += 1
    if nex == len(msg) :
        answer.append((dic[msg[cur:nex]]))
        break

    # 만약 [현재글자 + 다음글자]가 사전에 없으면
    if msg[cur:nex + 1] not in dic:
        idx += 1
        dic[msg[cur:nex + 1]] = idx  # 사전에 추가
        answer.append(dic[msg[cur:nex]])
        cur = nex  # 현재글자를 다음글자로 옮겨줌
print(answer)