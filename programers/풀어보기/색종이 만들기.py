n = int(input())
graph = []
for i in range(n) :
    graph.append(list(map(int,input().split())))

white, blue = 0, 0

def check(row,col,n) :
    global white, blue
    cur = graph[row][col]
    for i in range(row,row+n) :
        for j in range(col,col+n) :
            if cur != graph[i][j] :
                check(row+n//2, col+n//2, n//2)
                check(row+n//2, col, n//2)
                check(row, col+n//2, n//2)
                check(row, col, n//2)
                return
    if cur == 0 :
        white += 1
    else :
        blue += 1
    return

check(0,0,n)
print(white)
print(blue)