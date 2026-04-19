import sys
input = sys.stdin.readline
n = int(input().rstrip())

timeline = []

for i in range(n) :
    start, end = map(int,input().rstrip().split())
    timeline.append((start,end))

timeline.sort(key = lambda x : (x[1],x[0]))

endtime = timeline[0][1]
cnt = 1

for i in range(1,n) :
    if timeline[i][0] >= endtime :
        cnt += 1
        endtime = timeline[i][1]
print(cnt)