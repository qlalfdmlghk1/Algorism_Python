x = int(input())
line = 1
while x > line :
    x -= line
    line += 1

if line % 2 == 0 :
    a = x
    b = line + 1 - x
else :
    b = x
    a = line + 1 - x
print(f"{a}/{b}")
