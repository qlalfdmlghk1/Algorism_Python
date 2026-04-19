import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    flag = 1
    n = int(input())
    numbers = []
    for _ in range(n) :
        numbers.append(input().strip())
    numbers.sort()  # numbers = ['911','97625999','91125426']
    # print(numbers)

    for i in range(1,n) :
        # print(numbers[i-1])
        # print(numbers[i][:len(numbers[i-1])])
        if numbers[i-1] == numbers[i][:len(numbers[i-1])] :
            flag = 0
            break

    if flag == 0 : print("NO")
    else : print("YES")