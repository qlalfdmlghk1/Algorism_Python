import math
a,b = map(int,input().split())
num_a = int('1' * a)
num_b = int('1' * b)

print(math.gcd(num_a,num_b))