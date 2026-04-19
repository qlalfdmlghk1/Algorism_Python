n,k = map(int,input().split())  # 전체 날짜, 연속적인 날짜
temperature = list(map(int,input().split()))

prefix = [temperature[0]]
for i in range(1,n) :
    prefix.append(prefix[i-1] + temperature[i])
prefix.insert(0,0)

answer = -1e9
for i in range(k,n+1) :
    answer = max(answer, prefix[i] - prefix[i-k])
print(answer)