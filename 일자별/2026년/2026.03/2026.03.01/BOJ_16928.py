from collections import deque
N,M = map(int,input().split())
dict = {}

for _ in range(N) :
    a,b = map(int,input().split())
    dict[a] = b
    
for _ in range(M) :
    a,b = map(int,input().split())
    dict[a] = b

def bfs(start) :
    q = deque()
    q.append(start)
    visited = [False] * (101)
    visited[start] = 0
    while q :
        # print(q)
        cur = q.popleft()
        if cur == 100 :
            # print(visited)
            return visited[cur]
        for i in range(1,7) :
            nex = cur + i
            if 1 <= nex <= 100 :
                if nex in dict :
                    nex = dict[nex]
                if not visited[nex] :
                    q.append(nex)
                    visited[nex] = visited[cur] + 1

print(bfs(1))
