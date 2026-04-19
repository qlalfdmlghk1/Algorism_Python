g = int(input())
p = int(input())
airplanes = []
for _ in range(p) :
    airplanes.append(int(input()))

alters = list(range(g+1))  # 대안 게이트

def findSet(airplane):
    if alters[airplane] != airplane :
        return findSet(alters[airplane])
    return airplane

def union(root):
    # b is bigger
    b_root = findSet(root-1)
    alters[root] = b_root

cnt = 0

for i in range(p):
    airplane = airplanes[i]
    root = findSet(airplane)

    if root == 0:
        break

    union(root)
    cnt += 1

print(cnt)