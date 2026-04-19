from collections import defaultdict
n = int(input())
dic = defaultdict()
nums1 = list(map(int,input().split()))
for i in nums1 :
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1
m = int(input())
nums2 = list(map(int,input().split()))

answer = []
for i in nums2 :
    if i in dic :
        answer.append(dic[i])
    else :
        answer.append(0)
for i in answer:
    print(i, end=' ')