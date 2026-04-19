n = int(input())
parent = list(map(int,input().split()))

tree = [[] for _ in range(n)]
for i in range(1,n) :
    tree[parent[i]].append(i)

def dfs(node) :
    times = []  # 뉴스 전달 완료 시간

    for child in tree[node] :
        times.append(dfs(child))

    times.sort(reverse = True)

    max_time = 0  # 현재 노드가 뉴스 전파를 마치기까지 걸리는 최대 시간
    for i in range(len(times)) :
        max_time = max(max_time, times[i] + i + 1)

    return max_time

print(dfs(0))