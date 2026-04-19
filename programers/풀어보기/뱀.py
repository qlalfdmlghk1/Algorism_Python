from collections import deque
n = int(input())
k = int(input())

graph = [[0 for i in range(n)] for i in range(n)]
q = deque()
q.append((0,0))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0
cur_x,cur_y = 0,0
dix_index = 0
dic = {}

for i in range(k) :
    apple_row,apple_col = map(int,input().split())
    graph[apple_row-1][apple_col-1] = 'A'

l = int(input())

for i in range(l) :
    x,c = input().split()
    x = int(x)
    dic[x] = c

while True :
    cnt += 1
    cur_x += dx[dix_index]
    cur_y += dy[dix_index]
    if 0 > cur_x or cur_x >= n or cur_y < 0 or cur_y >= n :
        break

    if graph[cur_y][cur_x] == 'A':
        graph[cur_y][cur_x] = 1
        q.append((cur_y,cur_x))
        if cnt in dic and dic[cnt] == 'L' :
            dix_index = (dix_index - 1) % 4
        elif cnt in dic and dic[cnt] == 'D':
            dix_index = (dix_index + 1) % 4
    elif graph[cur_y][cur_x] == 0 :
        graph[cur_y][cur_x] = 1
        q.append((cur_y, cur_x))
        last_y,last_x = q.popleft()
        graph[last_y][last_x] = 0
        if cnt in dic and dic[cnt] == 'L':
            dix_index = (dix_index - 1) % 4
        elif cnt in dic and dic[cnt] == 'D':
            print('ture')
            dix_index = (dix_index + 1) % 4

    else :
        break
print(cnt)
