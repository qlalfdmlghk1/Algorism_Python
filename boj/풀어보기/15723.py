from collections import defaultdict
n = int(input())
graph = [[] for _ in range(26)]


for _ in range(n) :
    s1,s2 = map(str, input().strip().split(" is "))
    s1 = ord(s1) - ord('a')
    s2 = ord(s2) - ord('a')
    graph[s1].append(s2)

def dfs(x1,x2,graph,visited) :
    if x1 == x2 :
        return True
    visited[x1] = True

    for nex in graph[x1]:
        if not visited[nex]:
            if dfs(nex, x2, graph, visited):
                return True
    return False


m = int(input())
for _ in range(m) :
    r1,r2 = map(str, input().strip().split(" is "))
    r1 = ord(r1) - ord('a')
    r2 = ord(r2) - ord('a')
    visited = [False] * 26
    if dfs(r1,r2,graph,visited) :
        print("T")
    else :
        print("F")