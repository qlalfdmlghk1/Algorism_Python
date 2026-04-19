# from collections import deque
t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    papers = list(enumerate(list(map(int, input().split()))))
    v = papers[m]
    idx = 0
    while len(papers) :
       max_v = max([i[1] for i in papers])
       if papers[0][1] == max_v :
           now = papers.pop(0)
           idx += 1
           if now == v :
              print(idx)
              break
       else :
           now = papers.pop(0)
           papers.append(now)


