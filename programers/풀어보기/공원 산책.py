# 지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책.
# 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 ["방향 거리", "방향 거리" … ]과 같은 형식.
# 예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미.
#
# 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인.
# 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인.
# 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인.
# 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행.
#
# 공원의 가로 길이가 W, 세로 길이가 H.
# 공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때,
# 로봇 강아지가 모든 명령을 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return.
#
# park[i]는 다음 문자들로 이루어져 있으며 시작지점은 하나만 주어집니다.
# S : 시작 지점
# O : 이동 가능한 통로
# X : 장애물
#
# routes의 원소는 "op n"과 같은 구조. op는 이동할 방향, n은 이동할 칸의 수를 의미. op는 다음 네 가지중 하나.
# N : 북쪽으로 주어진 칸만큼 이동.
# S : 남쪽으로 주어진 칸만큼 이동.
# W : 서쪽으로 주어진 칸만큼 이동.
# E : 동쪽으로 주어진 칸만큼 이동.
#
# 입출력 예
# park	routes	result
# ["SOO","OOO","OOO"]	["E 2","S 2","W 1"]	[2,1]
# ["SOO","OXX","OOO"]	["E 2","S 2","W 1"]	[0,1]
# ["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]
park, routes = ["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]
m = len(park)
n = len(park[0])
result = []

def start(y,x) :
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        check_y = y
        check_x = x
        check_distance = distance
        if direction == 'E':
            check_x += 1
            while check_distance > 0 and 0 <= check_y < m and 0 <= check_x < n and park[check_y][check_x] != 'X':
                check_x += 1
                check_distance -= 1
                if check_distance == 0 :
                    x += distance

        elif direction == 'N':
            check_y -= 1
            while check_distance > 0 and 0 <= check_y < m and 0 <= check_x < n and park[check_y][check_x] != 'X':
                check_y -= 1
                check_distance -= 1
                if check_distance == 0:
                    y -= distance

        elif direction == 'W':
            check_x -= 1
            while check_distance > 0 and 0 <= check_y < m and 0 <= check_x < n and park[check_y][check_x] != 'X':
                check_x -= 1
                check_distance -= 1
                if check_distance == 0:
                    x -= distance

        elif direction == 'S':
            check_y += 1
            while check_distance > 0 and 0 <= check_y < m and 0 <= check_x < n and park[check_y][check_x] != 'X':
                check_y += 1
                check_distance -= 1
                if check_distance == 0:
                    y += distance

    result.append(y)
    result.append(x)
    print(result)

for i in range(m):
    for j in range(n) :
        if park[i][j] == 'S' :
            start(i,j)
