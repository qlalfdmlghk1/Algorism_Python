N = int(input())
distance = list(map(int,input().split()))
gases = list(map(int,input().split()))

min_gases = []
mini = int(1e9)
for gas in gases :
    if gas < mini :
        mini = gas
    min_gases.append(mini)

answer = 0
for i,dis in enumerate(distance) :
    answer += (dis * min_gases[i])
print(answer)