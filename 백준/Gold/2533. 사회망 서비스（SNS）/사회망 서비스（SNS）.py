import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 1992
def solve(v):
    global ans
    dp[v][1] = 1
    for nv in graph[v]:
        if visited[nv] == 0:
            visited[nv] = 1
            solve(nv)
            dp[v][0] += dp[nv][1]
            dp[v][1] += min(dp[nv][0], dp[nv][1])

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(N+1)
visited[1] = 1
# dp[v][0] = v가 얼리어답터가 아닐 때 자식들 중 얼리어답터의 개수
# dp[v][1] = v가 얼리어답터일 때 자식들 중 얼리어답터의 개수(본인 포함)
dp = [[0, 0] for _ in range(N+1)]
solve(1)
print(min(dp[1]))
