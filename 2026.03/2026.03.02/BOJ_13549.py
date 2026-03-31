import sys
input = sys.stdin.readline
from collections import deque
N,K = map(int, input().split())  # 수빈, 동생
MAX = 100_001
dist = [-1] * MAX

def bfs(start) :
    q = deque()
    q.append(start)
    dist[start] = 0
    while q :
        cur = q.popleft()
        if cur == K :
            return dist[cur]
            
        for nex,cost in [(cur*2,0), (cur-1,1), (cur+1,1)] :
            if 0 <= nex < MAX and dist[nex] == -1 :
                dist[nex] = dist[cur] + cost
                if cost == 0 :
                    q.appendleft(nex)
                else :
                    q.append(nex)
            
        
print(bfs(N))