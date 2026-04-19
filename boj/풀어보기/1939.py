from collections import deque
n,m = map(int, input().split())  # n : 섬의 개수, m : 다리의 수
bridge = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b,c = map(int, input().split())
    bridge[a].append([b,c])
    bridge[b].append([a,c])
s,d = map(int, input().split())

def bfs(weight):
	q = deque()
	q.append(s)
	visited = [False] * (n+1)
	visited[s] = True

	while q:
		x= q.popleft() # w == limit

		for i,w in bridge[x]:
			if not visited[i] and w >= weight:
				visited[i] = True
				q.append(i)

	if visited[d]:
		return True
	else:
		return False

start = 0
end = 1000000000

while start <= end :
    mid = (start + end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)