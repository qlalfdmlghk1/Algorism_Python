n,results = 5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n,results) :
    graph = [[0] * (n+1) for _ in range(n+1)]
    for a,b in results :
        graph[a][b] = 1
        graph[b][a] = -1

    for k in range(n+1) :
        for i in range(n+1) :
            for j in range(n+1) :
                if graph[i][j] == 0 :
                    if graph[i][k] == 1 and graph[k][j] == 1 :
                        graph[i][j] = 1
                    elif graph[i][k] == -1 and graph[k][j] == -1 :
                        graph[i][j] = -1
    answer = 0
    for g in graph :
        if g.count(0) == 2 :
            answer += 1
    return answer


print(solution(n,results))