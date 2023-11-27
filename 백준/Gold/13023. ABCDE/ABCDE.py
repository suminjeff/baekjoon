import sys
input = sys.stdin.readline


def dfs(depth, v):
    global ans
    if depth == 5:
        ans = 1
        return
    for w in relations[v]:
        if not visited[w]:
            visited[w] = 1
            dfs(depth+1, w)
            visited[w] = 0


N, M = map(int, input().split())
relations = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

ans = 0
for i in range(N):
    visited = [0]*N
    visited[i] = 1
    dfs(1, i)
    if ans:
        break
print(ans)