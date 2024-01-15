import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 20303


def dfs(v, depth):
    global res
    if visited[v] == 0:
        visited[v] = g
        relation[g][0] += 1
        relation[g][1] += C[v]
        for nv in graph[v]:
            dfs(nv, depth+1)


N, M, K = map(int, input().split())
C = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
group, g = [0]*(N+1), 1
visited = [0]*(N+1)
relation = {}
for i in range(1, N+1):
    if visited[i] == 0:
        relation.setdefault(g, [0, 0])
        dfs(i, 0)
        g += 1
knapsack = [[0]*(K+1) for _ in range(g)]
for i in range(1, g):
    f, c = relation[i]
    for j in range(1, K+1):
        if j < f:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-f]+c)
print(knapsack[g-1][K-1])