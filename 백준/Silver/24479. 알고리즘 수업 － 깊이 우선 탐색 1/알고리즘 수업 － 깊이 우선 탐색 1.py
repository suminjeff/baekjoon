import sys

sys.setrecursionlimit(10**5)

n, m, r = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

for node in range(1, n+1):
    graph[node].sort()

visited = [0]*(n+1)

order = 1
answer = [0]*(n+1)
answer[r] = 1

def dfs(v):
    global order
    visited[v] = 1
    answer[v] = order
    order += 1
    for nv in graph[v]:
        if visited[nv] == 0:
            dfs(nv)

dfs(r)

print(*answer[1:])