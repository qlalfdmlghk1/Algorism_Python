import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

arr = []
while True :
    try :
        arr.append(int(input()))
    except :
        break

def tree(start,end) :
    if start > end:
        return
    mid = end + 1
    for i in range(start+1,end+1) :
        if arr[i] > arr[start] :
            mid = i
            break
    tree(start+1,mid-1)
    tree(mid,end)
    print(arr[start])

tree(0,len(arr)-1)
