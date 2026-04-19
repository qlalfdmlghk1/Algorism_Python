n,lighthouse = 10,[[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]

from collections import deque,defaultdict
def solution(n, lighthouse):
    graph = defaultdict(list)
    onoff = [0 for _ in range(n+1)]  # 등대 on/off 여부 (1번부터 n번까지)

    for l in lighthouse :
        a,b = l
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    # 리프 노드라면, q에 담기
    for i in range(1,n+1) :
        if len(graph[i]) == 1 :
            q.append(i)

    while q :
        cur = q.popleft()

        # 이미 제거된 노드이면 무시
        if not graph[cur] :
            continue

        parent = graph[cur][0] # 이미 cur이 leaf 노드이니까 연결된 것은 부모 노드 밖에 없음

        del graph[cur]
        graph[parent].remove(cur)

        if len(graph[parent]) == 1 :
            q.append(parent)

        # 만약 지금 리프가 켜져 있다면 부모는 켤 필요 없음
        if onoff[cur] == 1:
            continue

        # 아니라면, 부모를 켜야 리프가 신호를 받을 수 있음
        onoff[parent] = 1

    return sum(onoff)

print(solution(n,lighthouse))