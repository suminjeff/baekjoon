import sys
input = sys.stdin.readline


def dfs(i, j, v):
    global cnt
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1':
            if visited[ni][nj] == 0:
                visited[ni][nj] = v
                cnt += 1
                dfs(ni, nj, v)


N = int(input())
arr = [input().rstrip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
v = 0

res = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visited[i][j] == 0:
            cnt = 1
            v += 1
            visited[i][j] = v
            dfs(i, j, v)
            res.append(cnt)
res.sort()
print(v)
for i in res:
    print(i)