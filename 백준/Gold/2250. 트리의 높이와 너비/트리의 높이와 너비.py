import sys
input = sys.stdin.readline


def dfs(level, node):
    global n, max_level
    left, right = graph[node]
    for next_node in left:
        if not visited[next_node]:
            dfs(level+1, next_node)
    if level not in res.keys():
        res.setdefault(level, [])
    res[level].append(n)
    n += 1
    for next_node in right:
        if not visited[next_node]:
            dfs(level+1, next_node)
    max_level = max(max_level, level)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    parent[y] = x


def get_root():
    for v in range(1, N+1):
        if parent[v] == v:
            return v


N = int(input())
graph = [[[] for _ in range(2)] for _ in range(N+1)]
parent = [i for i in range(N+1)]
visited = [False]*(N+1)
for _ in range(N):
    v, left, right = map(int, input().split())
    if left != -1:
        graph[v][0].append(left)
        union(v, left)
    if right != -1:
        graph[v][1].append(right)
        union(v, right)

res = {}
n = 1
max_level = 0
dfs(1, get_root())
ans = -1
max_diff = 0
for level in range(1, max_level+1):
    if max_diff < max(res[level]) - min(res[level]) + 1:
        max_diff = max(res[level]) - min(res[level]) + 1
        ans = level
print(ans, max_diff)