import sys
input = sys.stdin.readline

graph = []
for _ in range(9) :
    graph.append(list(map(int,input().split())))

check_list = []  # 아직 체워지지 않은 좌표들
for i in range(9) :
    for j in range(9) :
        if graph[i][j] == 0 :
            check_list.append((i,j))

# 세로줄 체크
def check_row(r,c) :
    nums = [1] * 9
    for i in range(9) :
        if graph[i][c] == 0 :
            if i == r :  # 다른 0이 있으면
                continue
            else :
                return False
        else :
            nums[graph[i][c]-1] -= 1
    for idx,n in enumerate(nums) :
        if n == 1 :
            graph[r][c] = idx + 1
    return True


# 가로줄 체크
def check_colum(r,c) :
    nums = [1] * 9
    for j in range(9) :
        if graph[r][j] == 0:
            if j == c:
                continue
            else :  # 다른 0이 있으면
                return False
        else :
            nums[graph[r][j]-1] -= 1
    for idx,n in enumerate(nums) :
        if n == 1 :
            graph[r][c] = idx + 1
    return True

# 사각형 체크
def check_square(r,c) :
    nums = [1] * 9
    # 1영역
    if 0 <= r < 3 and 0 <= c < 3 :
        for i in range(3) :
            for j in range(3) :
                if graph[i][j] == 0 :
                    if r != i or c != j :
                        return False
                    else :
                        continue
                else:
                    nums[graph[i][j]-1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 2영역
    if 3 <= r < 6 and 0 <= c < 3 :
        for i in range(3,6) :
            for j in range(3) :
                if graph[i][j] == 0:
                    if r != i or c != j:
                        return False
                    else:
                        continue
                else:
                    nums[graph[i][j]-1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 3영역
    if 6 <= r < 9 and 0 <= c < 3 :
        for i in range(6,9) :
            for j in range(3) :
                if graph[i][j] == 0:
                    if r != i or c != j:
                        return False
                    else:
                        continue
                else:
                    nums[graph[i][j]-1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 4영역
    if 0 <= r < 3 and 3 <= c < 6 :

        for i in range(3):
            for j in range(3,6):
                if graph[i][j] == 0:
                    if r != i or c != j :
                        return False
                    else :
                        continue
                else:
                    nums[graph[i][j]-1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 5영역
    if 3 <= r < 6 and 3 <= c < 6 :
        for i in range(3, 6):
            for j in range(3,6):
                if graph[i][j] == 0:
                    if r != i or c != j:
                        return False
                    else:
                        continue
                else:
                    nums[graph[i][j] - 1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 6영역
    if 6 <= r < 9 and 3 <= c < 6:
        for i in range(6,9):
            for j in range(3,6):
                if graph[i][j] == 0:
                    if r != i or c != j:
                        return False
                    else:
                        continue
                else:
                    nums[graph[i][j] - 1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 7영역
    if 0 <= r < 3 and 6 <= c < 9 :
        for i in range(3):
            for j in range(6,9):
                if graph[i][j] == 0:
                    if r != i or c != j:
                        return False
                    else:
                        continue
                else:
                    nums[graph[i][j] - 1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 8영역
    if 3 <= r < 6 and 6 <= c < 9:
        for i in range(3,6):
            for j in range(6,9):
                if graph[i][j] == 0:
                    if r != i or c != j:
                        return False
                    else:
                        continue
                else:
                    nums[graph[i][j] - 1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True
    # 9영역
    if 6 <= r < 9 and 6 <= c < 9:
        for i in range(6,9):
            for j in range(6,9):
                if graph[i][j] == 0:
                    if r != i or c != j:
                        return False
                    else:
                        continue
                else:
                    nums[graph[i][j] - 1] -= 1
        for idx, n in enumerate(nums):
            if n == 1:
                graph[r][c] = idx + 1
        return True

while check_list :
    r,c = check_list.pop(0)
    if not check_row(r,c) and not check_colum(r,c) and not check_square(r,c) :
        check_list.append((r,c))

for g in graph :
    print(*g)