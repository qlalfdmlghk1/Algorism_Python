from itertools import permutations
arr	= ["1", "-", "3", "+", "5", "-", "8"]
dic = {'+','-'}
plmi = []
nums = []
dp = {}
for i in arr :
    if i in dic :
        plmi.append(i)
    else :
        nums.append(i)

for i in permutations(plmi,len(plmi)) :
    if i in dp :
        continue
    else :
        dp[i] = dp.get(i)
        for num in nums :
            num 