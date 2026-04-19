# 조합? # 백트래킹?
# 이 문제는 서브트리의 가중치 합을 구하는 문제라고 한다 -> dfs와 dp 로 풀 수 있음
# dp[n][1] -> n번 마을을 우수마을로 선정했을 경우 우수 마을의 주민 수의 총합
# dp[n][0] -> n번 마을을 우수마을로 선정하지 않았을 경우 우수 마을의 주민 수의 총합
import collections,sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# DP
# dfs> u번 마을을 방문하지 않았다면 u번 마을을 방문
# 1. n번 마을을 선정했을 경우 인접한 u번 마을을 선정할 수 없다  => dp[n][1] += dp[u][0]
# 2. n번 마을을 선정하지 않았을 경우, 인접한 u번 마을을 선정하거나 선정하지 않는 2가지 경우 모두 고려  => dp[n][0] += max(dp[u][0], dp[u][1])
n = int(input())
people = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dic = collections.defaultdict(list)
people = [0] + people  # index[0] 처리해줘야 함
dp = []

for i in range(n+1) :
    dp.append([0, people[i]] )  # dp[i][0] = i(마을 선정x), dp[i][1] = i(마을 선정o)

for _ in range(n-1) :
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)
def dfs(cur) :
    visited[cur] = True
    for nex in dic[cur] :
        if not visited[nex] :
            dfs(nex)
            dp[cur][1] += dp[nex][0]  # 현재 마을을 우수마을로 선정
            dp[cur][0] += max(dp[nex][0], dp[nex][1])  # 현재 마을을 우수마을로 선정

dfs(1)
print(max(dp[1][1], dp[1][0]))