from collections import deque

T = int(input())


for _ in range(T) :
    N,M = map(int,input().split())
    q = deque(enumerate(map(int,input().split())))  # (원래 인덱스, 우선순위)
    cnt = 0
    
    while q :
        idx, pri = q.popleft()
        if any(p > pri for _,p in q) :
            q.append((idx,pri))
        else :
            cnt += 1
            if idx == M :
                print(cnt)
                break