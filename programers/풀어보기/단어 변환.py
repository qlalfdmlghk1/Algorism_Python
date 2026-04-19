begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque

q = deque()
visited = {}
visited[begin] = 0
for i in words :
    visited[i] = 0

def bfs(b,t) :
    q.append(b)
    while q :
        print(q)
        print(visited)
        cur = q.popleft()
        if cur == t :
            print(visited[cur])
            break
        for word in words :
            cnt = 0
            for i in range(len(cur)) :
                if cur[i] != word[i] :
                    cnt += 1
            if cnt == 1 and visited[word] == 0:
                visited[word] = visited[cur] + 1
                q.append(word)

if target not in words :
    print(0)
else :
    bfs(begin,target)