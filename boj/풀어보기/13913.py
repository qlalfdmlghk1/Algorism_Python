from collections import deque
MAX = 100001
places = [-1]  * (MAX)
pre = [-1] * (MAX)  # 해당 index 로 오기 전에 어디 밟았는지
soobin, brother = map(int, input().split())

q = deque()

def find_brother(start,target) :
    q.append(start)
    places[start] = 0
    while q :
        cur = q.popleft()
        for nex in (cur * 2, cur - 1, cur + 1) :
            if 0 <= nex <= MAX and places[nex] == -1:  # 경계 & 미방문 먼저
                places[nex] = places[cur] + 1
                pre[nex] = cur
                if nex == target:  # 방문 처리 후 조기 종료
                    return places[cur] + 1
                q.append(nex)
    return 0

cnt = 0
cnt = find_brother(soobin,brother)

q2 = deque()
route = []
def find_route(x) :
    q2.append(x)
    while q2 :
        cur = q2.popleft()
        route.append(cur)
        q2.append(pre[cur])
        if cur == soobin :
            break

find_route(brother)
route.reverse()

print(cnt)
for r in route :
    print(r,end=" ")