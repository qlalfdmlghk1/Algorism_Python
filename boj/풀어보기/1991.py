from collections import defaultdict
n = int(input())
graph = defaultdict(list)

for _ in range(n) :
    c,l,r = map(str,input().split())
    graph[c].append((l,r))
print(graph)

def preOrder(root) :
    if graph[root][0] == "." and graph[root][1] == "." :
        print(root)
    preOrder(graph[root][0])

def inOrder(root) :
    if graph[root][0] != "." and graph[root][1] != "." :
        print(root)
    else :
        inOrder(graph[root][0])

def postOrder(root) :
    if graph[root][0] == "." and graph[root][1] == "." :
        print(root)
    else :
        postOrder(graph[root][0])