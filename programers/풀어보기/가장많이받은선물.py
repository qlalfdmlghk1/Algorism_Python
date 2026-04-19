friends	= ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

gifted = {}  # gifted = {"friend 이름": {"선물 준 친구 이름": 이 친구에게 준 선물 개수}}
gift_idx = {}

for friend in friends:
    gifted[friend] = {}
    gift_idx[friend] = 0

for gift in gifts:
    t, f = gift.split(' ')  # t: 선물을 준 사람, f: 받은 사람
    if f in gifted[t]:
        gifted[t][f] += 1
    else:
        gifted[t][f] = 1
    # 선물 지수 반영
    gift_idx[t] += 1
    gift_idx[f] -= 1

# 각자 받게 될 선물 개수
will_get = [0 for _ in friends]  # friends 리스트 순서대로 저장

for i in range(len(friends)):
    cur = friends[i]  # 인덱스 i에 해당하는 친구
    for j in range(i + 1, len(friends)):
        another = friends[j]  # 인덱스 j에 해당하는 친구
        # cur가 another에게 준 선물 개수
        a = gifted[cur][another] if another in gifted[cur] else 0
        # another가 cur에게 준 선물 개수
        if cur in gifted[another] :
            b = gifted[another][cur]
        else :
            b = 0

        if a > b:    # cur가 선물을 더 많이 줬다면
            will_get[i] += 1
        elif a < b:  # another가 선물을 더 많이 줬다면
            will_get[j] += 1
        elif a == b:  # 둘이 선물을 주고 받은 개수가 같다면
            ai, bi = gift_idx[cur], gift_idx[another]
            if ai > bi:
                will_get[i] += 1
            elif ai < bi:
                will_get[j] += 1

answer = max(will_get)
print(answer)