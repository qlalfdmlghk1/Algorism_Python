import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
pocket = {}
for i in range(n) :
    monster = input().rstrip()
    pocket[monster] = i+1
    pocket[str(i+1)] = monster

for j in range(m) :
    checking = input().rstrip()
    print(pocket[checking])