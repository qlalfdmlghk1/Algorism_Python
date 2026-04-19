n = 15
q = [[2, 3, 9, 12, 13]]
ans = [2]
m = len(q) - 1
answer = 0
from itertools import combinations
arr = [i for i in range(1,n+1)]
for i in combinations(arr,5) :
    flag = True
    for idx, code in enumerate(q) :
        cnt = 0
        print(i)
        for c in code :
            if c in i :
               cnt += 1
               print(c)
               print(cnt)
               if cnt > ans[idx] :
                   flag = False
                   break
        if cnt != ans[idx] :
            break
        if not flag :
            break
        if idx == m :
            answer += 1
    print("answer",answer)
print(answer)