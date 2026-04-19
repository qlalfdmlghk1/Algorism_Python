'''n,k = map(int,input().split())
stack = []
for i in range(1,n+1) :
    stack.append(i)
index = k-1
answer = []
cnt = 0
while stack :
    answer.append(str(stack.pop(index)))
    index += (k-1)
    while index > len(stack)-1 :
        if len(stack) == 1 :
            answer.append(str(stack.pop()))
            break
        index -= len(stack)

result = ', '.join(answer)
print(f'<{result}>')'''

'''n,k = map(int,input().split())
stack = []
for i in range(1,n+1) :
    stack.append(i)
index = k-1
answer = []
cnt = n
while stack :
    answer.append(str(stack.pop(index)))
    cnt -= 1
    index += (k-1)
    while index > cnt-1 :
        if cnt == 1 :
            answer.append(str(stack.pop()))
            break
        index -= cnt

result = ', '.join(answer)
print(f'<{result}>')'''

from collections import deque
q = deque()
n,k = map(int,input().split())
stack = []
for i in range(1,n+1) :
    q.append(str(i))

answer = []

while q :
    for _ in range(k-1) :
        q.append(q.popleft())
    answer.append(q.popleft())

result = ', '.join(answer)
print(f'<{result}>')