n = int(input())
stack = []
for i in range(n) :
    k = int(input())
    if k == 0 :
        stack.pop()
    else :
        stack.append(k)
print(sum(stack))