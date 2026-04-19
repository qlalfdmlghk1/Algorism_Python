from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
cost = [0] * (n+1)

for i in range(1,n+1) :
    building = list(map(int,input().split()))[:-1]
    time = building.pop(0)
    cost[i] = time
    for b in building :
        graph[b].append(i)
        indegree[i] += 1

q = deque()
for i in range(1,n+1) :
    if indegree[i] == 0 :  # 먼저 처리해야될 건물이 없는 경우
        q.append(i)

result = [0] * (n+1)
while q :
    cur = q.popleft()
    result[cur] += cost[cur]  # 현재 건물 짓는 시간 더해주기
    for nex in graph[cur] :
        indegree[nex] -= 1
        result[nex] = max(result[nex],result[cur])  # 선행 건물 중 가장 늦게 끝난 시간 업데이트
        if indegree[nex] == 0 :
            q.append(nex)  # 선행 건물이 없는 경우 queue에 넣기

for i in result[1:] :
    print(i)