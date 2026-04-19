n = int(input())
seats = list(input())
cups = [False] * (n+1)
# stack = ["C"]
index = 0
cant = 0

# for i in range(2,n) :
#     if seats[i-2] == "L" and seats[i-1] == "L" and seats[i] == "L" :
#         if i != 2 and i != n-1 :
#             cant += 1

for i in range(1,n) :
    if seats[i-1] == "L" and seats[i] == "L" :
        cups[i] = True

for i in range(n) :
    if not cups[i] :
        cups[i] = True
    elif not cups[i+1] :
        cups[i+1] = True
    else :
        cant += 1
    print(cant)
    print(cups)
print(n-cant)




# while index < n :
#     if stack[-1] == "C" :
#         stack.append(seats[index])
#         index += 1
#     elif stack[-1] == "S":
#         stack.append("C")
#     else :  # stack[-1] == "L":
#         if seats[index] == "S" :
