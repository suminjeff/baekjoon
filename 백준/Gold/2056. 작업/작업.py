import sys
input = sys.stdin.readline
from collections import deque

# 2056

N = int(input())
time, degree = [0]*(N+1), [0]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    t, k, *task = map(int, input().split())
    time[i] = t
    for j in range(k):
        degree[i] += 1
        graph[task[j]].append(i)

dp = [0]*(N+1)
que = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        que.append(i)
        dp[i] = time[i]
while que:
    v = que.popleft()
    for nv in graph[v]:
        degree[nv] -= 1
        dp[nv] = max(dp[v]+time[nv], dp[nv])
        if degree[nv] == 0:
            que.append(nv)
print(max(dp))