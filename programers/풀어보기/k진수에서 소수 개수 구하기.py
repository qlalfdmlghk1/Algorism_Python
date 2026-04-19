# 양의 정수 n. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.
#
# 1. 0P0처럼 소수 양쪽에 0이 있는 경우
# 2. P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 3. 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# 4. P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수.
# 예를 들어, 101은 P가 될 수 없습니다.
# 예를 들어, 437674을 3진수로 바꾸면 211020101011입니다.
# 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개. (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.)
# 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.
#
# 정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return.
#
# 1 ≤ n ≤ 1,000,000
# 3 ≤ k ≤ 10
#
# n	        k	result
# 437674	3	3
# 110011	10	2
#
# 입출력 예 #2
# 110011을 10진수로 바꾸면 110011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 11, 11 2개입니다.
# 이와 같이, 중복되는 소수를 발견하더라도 모두 따로 세어야 합니다.
n,k = 36,3
result = 0
def change(num) :
    new_num = ''
    NUMBER = '0123456789ABCDEF'
    if num == 0 :
        return '0'
    while num > 0 :
        a,b = divmod(num,k)
        new_num += NUMBER[b]
        num //= k
    return new_num[::-1]

def primenum(num) :
    if num == 1 :
        return False
    elif num == 2 :
        return True
    for i in range(2,int(num**0.5) + 2) :
        if num % i == 0 :
            return False
    return True

dic = ['00','000','0000','00000','000000','0000000']
new_num = change(n)
new_num = str(new_num)
for i in dic :
    new_num = new_num.replace(i,'0')

a = new_num.split('0')
# new_num.rstrip('0')
# print(new_num)
# print(a)
for i in a :
    if i and primenum(int(i)) :
        result += 1
print(result)
