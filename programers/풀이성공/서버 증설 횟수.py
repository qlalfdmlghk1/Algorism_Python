players,m,k = [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],1,1 # 이용자수,m명 마다 증설(포함),시간

def solution(players,m,k):
    answer = 0
    servers = [1 for _ in range(24)]
    for i in range(24) :
        while players[i] >= servers[i] * m :
            for j in range(k) :
                if i+j < 24 :
                    servers[i+j] += 1
            answer += 1
    return answer

print(solution(players, m, k))