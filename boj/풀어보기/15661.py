import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
grid = []
arr = []
result = 214700000

for i in range(n) :
  grid.append(list(map(int,input().split())))
  arr.append(i)


for i in range(1,n-1) :              # 팀을 나누는 조합의 크기는 1부터 n-1까지
  for r1 in combinations(arr, i) :
    start = 0
    link = 0
    r2 = list(set(arr)-set(r1))      # r2: 두 번째 팀은 전체 팀원에서 첫 번째 팀원을 제외한 인원들로 구성

    for r in combinations(r1, 2) :  # 첫 번째 팀에서 두 명을 선택하는 모든 조합에 대해
      start += grid[r[0]][r[1]]       # 두 사람의 능력치 합을 더함
      start += grid[r[1]][r[0]]       # 반대 방향의 능력치도 더함

    for r in combinations(r2, 2) :  # 두 번째 팀에서 두 명을 선택하는 모든 조합에 대해
      link += grid[r[0]][r[1]]        # 두 사람의 능력치 합을 더함
      link += grid[r[1]][r[0]]        # 반대 방향의 능력치도 더함

    result = min(result, abs(start-link))

print(result)