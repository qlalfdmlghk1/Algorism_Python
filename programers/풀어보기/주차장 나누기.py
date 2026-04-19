n,cars = 13,[22,9,1,15,8,6,20,7,11,5,10,4,1]
links = [[4,7],[13,10],[6,3],[7,1],[6,12],[5,11],[5,6],[5,10],[9,8],[8,11],[8,2],[7,8]]

from collections import defaultdict
cars_sum = [0] + cars
graph = defaultdict(list)

visited = [False for _ in range(len(cars) + 1)]
visited[1] = True

for link in links :
    graph[link[0]-1].append(link[1]-1)
    graph[link[1]-1].append(link[0]-1)

#✅스택에 루트 노드를 넣고 dfs를 진행한다.
stack = [1]
while stack:
    if graph[stack[-1]] and visited[graph[stack[-1]][-1]]:  #✅스택에 추가하려는 노드가 부모 노드인 경우 제거.
        graph[stack[-1]].pop()

    if graph[stack[-1]]:    #✅자식 노드가 있는 경우 스택에 다음 노드를 추가.
        tmp = graph[stack[-1]].pop()
        visited[tmp] = True
        stack.append(tmp)

    else:       #✅자식 노드가 없는 경우 해당 노드의 노드값을 부모 노드에 추가.
        tmp = stack.pop()
        if stack:
            cars_sum[stack[-1]] += cars_sum[tmp]

target = cars_sum[1] / 2
min_diff = target

for cars_per_node in cars_sum:      #✅저장된 노드 값들을 통해 정답을 찾는다.
    min_diff = min(min_diff, abs(target - cars_per_node))
print(int(min_diff * 2))