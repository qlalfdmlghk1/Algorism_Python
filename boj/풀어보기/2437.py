from collections import defaultdict
n = int(input())
weight = list(map(int,input().split()))
weight.sort()
print(weight)

target = 1

for w in weight:
    if target < w:
        break
    target += w

print(target)
