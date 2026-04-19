n = 4

def solution(n):
    answer = []
    triangles = [[0 for _ in range(i)] for i in range(1,n+1)]
    direction = 0
    num = 1
    r,c = -1,0
    for i in range(n) :  # 방향 바꿀 때 필요함
        for j in range(i,n) :  # 얼마나 채울건가 (n번째는 n개)
            if direction % 3 == 0 :
                r += 1
            elif direction % 3 == 1 :
                c += 1
            else :
                r -= 1
                c -= 1
            triangles[r][c] = num
            num += 1
        direction += 1

    for triangle in triangles :
        for t in triangle :
            answer.append(t)

    return answer

print(solution(n))