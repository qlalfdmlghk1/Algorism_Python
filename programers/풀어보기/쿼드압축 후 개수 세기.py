arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

def solution(arr):
    answer = []
    s = len(arr)

    def check_square(r,c,n) :
        nonlocal cnt_zero
        nonlocal cnt_one
        target = arr[r][c]
        for i in range(r,r+n) :
            for j in range(c,c+n) :
                if arr[i][j] != target :
                    check_square(r,c,n//2)
                    check_square(r+n//2,c,n//2)
                    check_square(r,c+n//2,n//2)
                    check_square(r+n//2,c+n//2,n//2)
                    return
        if target == 0 :
            cnt_zero += 1
        elif target == 1 :
            cnt_one += 1

    cnt_zero, cnt_one = 0, 0
    check_square(0,0,s)
    answer.append(cnt_zero)
    answer.append(cnt_one)
    return answer

print(solution(arr))