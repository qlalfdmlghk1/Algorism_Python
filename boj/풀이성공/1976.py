from collections import deque

n = int(input())
routes = [[i] for i in range(n+1)]
m = int(input())
for i in range(n) :
    arr = list(map(int, input().split()))
    for index,j in enumerate(arr) :
        if j == 1 :
            routes[i+1].append(index+1)

def bfs(start,end) :
    q = deque()
    q.append(start)
    visited = [False for _ in range(n+1)]
    visited[start] = True
    while q :
        cur = q.popleft()
        if cur == end:
            return True
        for nex in routes[cur] :
            if not visited[nex] :
                q.append(nex)
                visited[nex] = True
    return False

arr = list(map(int,input().split()))

answer = "YES"
for a in range(1,len(arr)) :
    if not bfs(arr[a-1],arr[a]) :
        answer = "NO"
print(answer)
