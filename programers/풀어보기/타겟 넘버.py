numbers	= [4, 1, 2, 1]
target = 4

from collections import deque

q = deque()
idx = 0

def bfs(n) :
    cnt = 0
    q.append([numbers[n], 0])
    q.append([-numbers[n], 0])
    while q :
        temp,idx = q.popleft()

        if idx == len(numbers) - 1 :
            if temp == target :
                cnt += 1
        else :
            idx += 1
            q.append([temp + numbers[idx], idx])
            q.append([temp - numbers[idx], idx])

    print(cnt)

bfs(0)
