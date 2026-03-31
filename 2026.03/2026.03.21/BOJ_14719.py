H,W = map(int,input().split())
blocks = list(map(int,input().split()))

left_max = [0] * W
right_max = [0] * W

left_max[0] = blocks[0]
right_max[W-1] = blocks[-1]

for i in range(1,W) :
    left_max[i] = max(blocks[0:i])
for i in range(W-2,-1,-1) :
    right_max[i] = max(blocks[i+1:W])

rain = 0
for i in range(1,W-1) :
    rain += max(0,min(left_max[i],right_max[i]) - blocks[i])
print(rain)