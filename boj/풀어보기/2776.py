t = int(input())

def binary_search(arr,target) :
    left = 0
    right = len(arr) - 1
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target :
            return 1
        else :
            if arr[mid] < target :
                left = mid + 1
            else :
                right = mid - 1
    return 0

for _ in range(t) :
    n = int(input())
    note1 = list(map(int,input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()
    for i in note2 :
        print(binary_search(note1,i))


