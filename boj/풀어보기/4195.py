t = int(input())

def findSet(x) :
    if parent[x] != x :
        return findSet(parent[x])
    return x

def union(a,b) :
    a = findSet(a)
    b = findSet(b)
    if a != b :
        parent[b] = a
        cnt[a] += cnt[b]

for _ in range(t) :
    f = int(input())
    parent = {}
    cnt = {}
    for _ in range(f):
        a, b = input().split()

        # 처음 등장하는 친구라면 초기화
        for person in [a, b]:
            if person not in parent:
                parent[person] = person
                cnt[person] = 1
        union(a, b)
        print(cnt[findSet(a)])
