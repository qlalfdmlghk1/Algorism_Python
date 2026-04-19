wallpaper = ["..", "#."]

def solution(wallpaper):
    answer = []
    min_x, min_y, max_x, max_y = int(1e9), int(1e9), 0, 0
    n,m = len(wallpaper), len(wallpaper[0])
    for i in range(n) :
        for j in range(m) :
            if wallpaper[i][j] == '#' :
                min_x = min(min_x,i)
                min_y = min(min_y,j)
                max_x = max(max_x,i)
                max_y = max(max_y,j)
    answer.append(min_x)
    answer.append(min_y)
    answer.append(max_x+1)
    answer.append(max_y+1)
    return answer

print(solution(wallpaper))