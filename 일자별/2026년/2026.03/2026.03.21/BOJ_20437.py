import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())

for _ in range(T) :
    W = input()
    K = int(input())
    
    if K == 1 :
        print(1,1)
        continue

    pos = defaultdict(list)
    for i,c in enumerate(W) :
        pos[c].append(i)
    
    min_len = int(1e9)
    max_len = 0

    for c in pos :  
        indices = pos[c]
        if len(indices) < K :
            continue

        for i in range(len(indices) - K + 1) :
            length = indices[i + K - 1] - indices[i] + 1
            min_len = min(min_len,length)
            max_len = max(max_len,length)
    
    if max_len == 0 :
        print(-1)
    else :
        print(min_len, max_len)