N,M,T = map(int,input().split()) # 정점, 간선, 연습 횟수

INF = int(1e9)
distance = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1) :
    distance[i][i] = 0

for _ in range(M) :
    u, v, h = map(int,input().split())
    distance[u][v] = min(distance[u][v],h)

for k in range(1,N+1) : 
    for i in range(1,N+1) : 
        for j in range(1,N+1) :
            distance[i][j] = min(distance[i][j], max(distance[i][k], distance[k][j]))

for _ in range(T) :
    s,e = map(int,input().split())
    print(-1 if distance[s][e] >= INF else distance[s][e])
