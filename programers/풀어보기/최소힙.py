from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
hq = []
n = int(input())
for i in range(n) :
    num = int(input().rstrip())
    if num == 0 :
        if not hq :
            print(0)
        else :
            print(heappop(hq))
    else :
        heappush(hq,num)
