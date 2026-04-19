blocks=[[0, 41]]
result=[41]

h = len(blocks)
dp = [[False] * i for i in range(1,h+1)]
answer = []
for index, block in enumerate(blocks) :
    dp[index][block[0]] = block[1]

for index,block in enumerate(blocks) :
    left,right = block[0],block[0]

    while left > 0 :
        dp[index][left-1] = dp[index-1][left-1] - dp[index][left]
        left -= 1
    while right < index :
        dp[index][right+1] = dp[index-1][right] - dp[index][right]
        right += 1

for i in range(h) :
    for j in range(i+1) :
        answer.append(dp[i][j])
print(answer)


