skill,skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]	# return = 2


cnt = len(skill_trees)
for trees in skill_trees :
    stack = [i for i in skill[::-1]]
    for i in trees :
        if i in stack :
            if stack[-1] == i :
                stack.pop()
            else :
                cnt -= 1
                break
print(cnt)

