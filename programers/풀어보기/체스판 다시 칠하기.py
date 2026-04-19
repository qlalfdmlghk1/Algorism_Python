n,m = map(int,input().split())
graph = []
answer = 214700000
for i in range(n) :
    graph.append(input())

for i in range(n-7) :
    for j in range(m-7) :
        cnt = 0
        cnt_1 = 0
        cnt_2 = 0
        for x in range(8) :
            for y in range(8) :
                new_x, new_y = i+x, j+y
                if (new_x + new_y) % 2 == 0 :
                    if graph[new_x][new_y] == 'W':
                        cnt_1 += 1
                    elif graph[new_x][new_y] == 'B':
                        cnt_2 += 1
                else :
                    if graph[new_x][new_y] == 'B':
                        cnt_1 += 1
                    elif graph[new_x][new_y] == 'W':
                        cnt_2 += 1
        cnt = min(cnt_1,cnt_2)
        answer = min(cnt,answer)
print(answer)


