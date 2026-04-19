n = int(input())
lines = []
degree = [0] * (n+1)
jTree = 0
dTree = 0

for _ in range(n-1) :
    u,v = map(int, input().split())
    lines.append((u,v))
    degree[u] += 1
    degree[v] += 1

# ㅈ 트리 : 하나의 노드를 기준으로 연결된 노드가 3개 이상일 때 그 중 3개 선택 nC3
# ㄷ 트리 : 연결된 두 노드를 기준으로 두 노드 각각에 연결된 노드의 수를 곱함

# ㅈ 트리 개수
for i in range(n-1) :
    if degree[i] >= 3 :
        jTree += degree[i] * (degree[i] - 1) * (degree[i] - 2) / 6

# ㄷ 트리 개수
for line in lines :
    u,v = line
    dTree += ((degree[u] - 1) * (degree[v] - 1))

if dTree > 3 * jTree :
    print("D")
elif dTree < 3 * jTree:
    print("G")
else:
    print("DUDUDUNGA")