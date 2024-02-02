import sys
input = sys.stdin.readline

from collections import deque

# 2623

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0]*(N+1)
for _ in range(M):
    S, *singer = map(int, input().split())
    for s in range(1, S):
        s1, s2 = singer[s-1], singer[s]
        graph[s1].append(s2)
        degree[s2] += 1
que = deque()
for d in range(1, N+1):
    if degree[d] == 0:
        que.append(d)
ans = []
while que:
    v = que.popleft()
    ans.append(v)
    for nv in graph[v]:
        degree[nv] -= 1
        if degree[nv] == 0:
            que.append(nv)
if len(ans) != N:
    print(0)
else:
    print(*ans, sep='\n')
