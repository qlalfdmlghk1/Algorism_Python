input_string = "string"
from collections import defaultdict

dic = defaultdict()
ans = []

stack = [input_string[0]]
for s in input_string[1:] :
    if stack[-1] != s :
        dic[stack[-1]] = True
        stack.append(s)
        if s in dic :
            ans.append(s)
if not ans :
    print("N")
else :
    ans = list(set(ans))
    ans.sort()
    print(''.join(ans))