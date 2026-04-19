board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h,w	= 0,1
# 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.
# h, w가 주어질 때 board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return
# 1. 정수를 저장할 변수 n을 만들고 board의 길이를 저장.
# 2. 같은 색으로 색칠된 칸의 개수를 저장할 변수 count를 만들고 0을 저장.
# 3. h와 w의 변화량을 저장할 정수 리스트 dh, dw를 만들고 각각 [0, 1, -1, 0], [1, 0, 0, -1]을 저장.
# 4. 반복문을 이용해 i 값을 0부터 3까지 1 씩 증가시키며 아래 작업을 반복합니다.
#     4-1. 체크할 칸의 h, w 좌표를 나타내는 변수 h_check, w_check를 만들고 각각 h + dh[i], w + dw[i]를 저장.
#     4-2. h_check가 0 이상 n 미만이고 w_check가 0 이상 n 미만이라면 다음을 수행.
#         4-2-a. board[h][w]와 board[h_check][w_check]의 값이 동일하다면 count의 값을 1 증가.
# 5. count의 값을 return.
dh = [0, 1, -1, 0]
dw = [1, 0, 0, -1]
color = board[h][w]
cnt = 0
for i in range(4) :
    next_h = h + dh[i]
    next_w = w + dw[i]
    if color == board[next_h][next_w] :
        cnt += 1
print(cnt)