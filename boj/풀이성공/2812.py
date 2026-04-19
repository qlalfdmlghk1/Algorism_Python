import sys
input = sys.stdin.readline

n,k = map(int,input().split())
number = str(input()).strip()
stack = [number[0]]
k_cnt = k
for num in number[1:] :
    while stack and stack[-1] < num and k_cnt > 0 :
        stack.pop()
        k_cnt -= 1
    stack.append(num)

result = ''
for s in stack :
    result += s

if len(result) > n-k :
    result = result[:n-k]
print(int(result))