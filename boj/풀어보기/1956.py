v,e = map(int,input().split())  # 마을, 도로

graph = [[1e9 for _ in range(v+1)] for _ in range(v+1)]

# for i in range(1,v+1) :
#     graph[i][i] = 0

for _ in range(e) :
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1,v+1) :
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 1e9
for i in range(1,v+1) :
    answer = min(answer,graph[i][i])
if answer == 1e9 :
    print(-1)
else :
    print(answer)