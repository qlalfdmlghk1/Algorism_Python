n,m = map(int,input().split())  # 학생 수, 키 비교 수

graph = [[int(1e9) for _ in range(n)] for _ in range(n)]

for i in range(n) :
    graph[i][i] = 0

for _ in range(m) :
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

dic = {}
for gra in graph :
    print(gra)
    for g in gra :
        if g in dic :
            dic[g] += 1
        else :
            dic[g] = 1
cnt = 0
for d in dic.items() :
    if d[1] == 1 :
        cnt += 1
print(cnt)