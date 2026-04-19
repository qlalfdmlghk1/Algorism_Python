import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
num = a
for _ in range(b) :
    num = num*b % c
print(num)