import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())

for _ in range(T) :
    W = input()
    K = int(input())

    dict = defaultdict(list)
    for i,w in enumerate(W) :
        dict[w].append(i)
    # print(dict)
    min_length = int(1e9)
    max_length = 0
    for c in dict :
        if len(dict[c]) < K :
            continue
        for i in range(len(dict[c])-K+1) :
            length = dict[c][i+K-1] - dict[c][i] + 1
            # print(c,length)
            min_length = min(min_length,length)
            max_length = max(max_length,length)
    
    if max_length == 0 :
        print(-1)
    else :
        print(min_length,max_length)