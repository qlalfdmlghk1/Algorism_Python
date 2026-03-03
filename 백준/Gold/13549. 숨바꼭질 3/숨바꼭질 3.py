import sys
input = sys.stdin.readline
from collections import deque
N,K = map(int,input().split())
MAX = 100_001
dist = [-1] * MAX

def bfs(start) :
    q = deque()
    q.append(start)
    dist[start] = 0
    while q :
        # print(q)
        cur = q.popleft()
        if cur == K :
            return dist[cur]
        for idx,i in enumerate([cur*2, cur-1, cur+1]) :
            nex = i
            if 0 <= nex < MAX and dist[nex] == -1 :
                if idx == 0 :
                    q.appendleft(nex)
                    dist[nex] = dist[cur]
                else :
                    q.append(nex)
                    dist[nex] = dist[cur] + 1

print(bfs(N))