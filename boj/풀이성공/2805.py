n,m = map(int,input().split())  # n : 나무의 수, m : 집으로 가져가려는 나무의 길이
trees = list(map(int,input().split()))

result = 0
left,right = 0,max(trees)
while left <= right :
    mid = (left+right) // 2
    length = 0
    for tree in trees :
        length += max(tree - mid,0)

    if length >= m :
        result = max(result,mid)
        left = mid + 1
    else :
        right = mid - 1
print(result)