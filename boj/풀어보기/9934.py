# from collections import deque
# k = int(input())
# nodes = list(map(int, input().split()))
# cnt = len(nodes)  # 3
# height = 0
# visited = [False for _ in range(cnt)]
# answer = [[] for _ in range(cnt)]
# q = deque()
# dif = 1
#
# def BT(idx, dif) :
#     l_idx = idx - dif
#     r_idx = idx + dif
#     if l_idx < 0 :
#         return
#
# while dif < cnt :
#     idx = cnt // 2  # 1
#     dif += 1
#     BT(idx, dif)

k = int(input())
nodes = list(map(int, input().split()))
cnt = len(nodes)  # 3
answer = [[] for _ in range(cnt)]

def makeTree(arr, x) :
    root = len(arr) // 2
    answer[x].append(arr[root])
    if root == 0 :
        return
    makeTree(arr[:root], x+1)
    makeTree(arr[root+1:], x+1)

makeTree(nodes, 0)
for i in range(k) :
    print(*answer[i])