# https://edder773.tistory.com/298
grid = []
for _ in range(10) :
    grid.append(list(map(int,input().split())))
paper = [5,5,5,5,5]
result = 26

# 유망 조건
def promise(a1, a2, b1, b2) :
    for i in range(a1, a2+1) :
        for j in range(b1, b2+1) :
            if not grid[i][j] :
                return False
    return True

# 색종이 붙이기 / 떼기
def attach(a1, a2, b1, b2, w) :
    for i in range(a1, a2+1) :
        for j in range(b1, b2+1) :
            paper[i][j] = w

def glue(p) :
    global result
    for y in range(a1,a2)
