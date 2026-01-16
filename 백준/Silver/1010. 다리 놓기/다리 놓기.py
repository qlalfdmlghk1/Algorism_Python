t = int(input())
for _ in range(t) :
    answer = 1
    n,m = map(int,input().split())

    for i in range(n) :
        answer *= (m-i)
        answer /= (i+1)
    print(int(answer))