n = int(input())
arr = list(map(int, input().split()))
s = int(input())

idx = 0

# 교환 가능한 횟수가 남아있고, 현재 인덱스가 배열의 길이보다 작다면
while s > 0 and idx < n :
    # 현재 인덱스부터 교환 가능한 범위 내에서 최대값의 인덱스를 찾음
    m = arr.index(max(arr[idx : idx+s+1]))

    # 최대값이 현재 인덱스와 다를 경우, 최대값과 그 앞의 값과 교환
    if m != idx :
        arr[m], arr[m-1] = arr[m-1], arr[m]  # 최대값과 그 전의 값을 교환
        s -= 1
    else :
        idx += 1  # 최대값이 이미 현재 인덱스에 있으므로 다음 인덱스로 이동
print(*arr)