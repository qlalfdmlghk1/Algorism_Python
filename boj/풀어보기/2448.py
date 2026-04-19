import sys
input = sys.stdin.readline

n = int(input())   # n번째 줄까지의 별을 출력할 것임

stars = [[' ']*2*n for _ in range(n)]

# 기본 : 높이 3인 삼각형
def recursion(i,j,size) :
    if size == 3 :
        stars[i][j] = "*"            # 꼭대기 별
        stars[i+1][j-1] = stars[i+1][j+1] = "*"  # 중간 줄의 별
        for k in range(-2,3) :
            stars[i+2][j-k] = "*"    # 마지막 줄의 별 (5개)
    else :
        newSize = size // 2
        recursion(i,j,newSize)  # 자기 기준 위 삼각형
        recursion(i+newSize, j-newSize, newSize)  # 자기 기준 왼쪽 삼각형
        recursion(i+newSize, j+newSize, newSize)  # 자기 기준 오른쪽 삼각형

recursion(0,n-1,n)
for star in stars :
    print("".join(star))