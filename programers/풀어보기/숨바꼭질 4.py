# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력.
# 둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력.
from collections import deque
n,k = map(int,input().split())
dp = [0] * (2*k)
dp[n] = 1
q = deque()

def bfs(v) :
    q.append(v)
    while q :
        cur = q.popleft()
        if cur == k :
            print(dp[cur])
            break
        else :
            for next in [2*cur,cur-1,cur+1] :
                if 0 <= next < 2*k and dp[next] == 0 :
                    dp[next] = dp[cur] + 1
                    q.append(next)

bfs(n)

