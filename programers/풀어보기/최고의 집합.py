# 1. 각 원소의 합이 S가 되는 수의 집합
# 2. 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합
# 예를 들어 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합은 다음과 같이 4개. -> { 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 }
# 그중 각 원소의 곱이 최대인 { 4, 5 }가 최고의 집합.
# 집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 return.
#
# 제한사항
# 1. 최고의 집합은 오름차순으로 정렬된 1차원 배열(list, vector) 로 return.
# 2. 만약 최고의 집합이 존재하지 않는 경우에 크기가 1인 1차원 배열(list, vector) 에 -1 을 채워서 return.
# 3. 자연수의 개수 n은 1 이상 10,000 이하의 자연수.
# 4. 모든 원소들의 합 s는 1 이상, 100,000,000 이하의 자연수

n,s = 2,8
result = []
div,mod = divmod(s,n)
if div == 0 :
    result.append(-1)
else :
    while mod != 0 :
        result.append(div)
        s -= div
        n -= 1
        div, mod = divmod(s, n)
    for i in range(n) :
        result.append(div)
print(result)
