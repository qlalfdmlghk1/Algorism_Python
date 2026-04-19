n = int(input())
cnt = 1
bricks = [[0,0,0,0]]
dp = [0] * (n+1)

# 밑면의 넓이, 벽돌의 높이 그리고 무게
for _ in range(n) :
    brick = list(map(int, input().split()))
    brick.append(cnt)
    bricks.append(brick)
    cnt += 1

bricks.sort(key = lambda x : x[0])  # 밑면 넓이 기준 정렬
# print(bricks)

for i in range(1,n+1) :
    for j in range(i) :
        # 현재 벽돌의 무게가 쌓여있는 벽돌보다 무겁다면
        if bricks[i][2] > bricks[j][2] :
            dp[i] = max(dp[i], bricks[i][1] + dp[j])
# print(dp)

max_value = max(dp)
index = n
result = []

while index != 0:
    # max_value 와 dp[index]가 같다면
    if max_value == dp[index]:
        result.append(bricks[index][3])
        # arr[index]값 추가 했으니 추가한 벽돌의 높이 값 빼기
        max_value = max_value - bricks[index][1]
    index -= 1


print(len(result))
for i in result[::-1] :
    print(i)