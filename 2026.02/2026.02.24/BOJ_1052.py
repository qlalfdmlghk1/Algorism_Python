N,K = map(int, input().split())

cnt = 0

while N :
    if N // 2 == 0 :
        N = N // 2
    else :
        N = N // 2 + 1
        cnt += 1

    if N == K :
        break
print(cnt)
    