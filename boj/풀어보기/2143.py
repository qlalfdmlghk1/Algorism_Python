from collections import Counter

t = int(input())
n = int(input())
a_list = list(map(int,input().split()))
m = int(input())
b_list = list(map(int,input().split()))

a_count_list = Counter(a_list)
b_count_list = Counter(b_list)

for i in range(n) :
    for j in range(i+1,n) :
        a_count_list[sum(a_list[i:j+1])] += 1

for i in range(m):
    for j in range(i+1, m):
        b_count_list[sum(b_list[i:j+1])] += 1

result = 0
for b in b_count_list :
    if t-b in a_count_list :
        result += a_count_list[t-b] * b_count_list[b]
print(result)