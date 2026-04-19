import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[int(1e9) for _ in range(n)] for _ in range(n)]

for i in range(n) :
    graph[i][i] = 0

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1],c)

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for gra in graph :
    for g in gra :
        if g == int(1e9) :
            g = 0
        print(g, end=" ")
    print()