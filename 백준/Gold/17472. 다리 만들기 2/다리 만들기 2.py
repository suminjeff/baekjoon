import sys
input = sys.stdin.readline


def dfs(n, r, c):
    visited[r][c] = 1
    arr[r][c] = n
    islands[n].append([r, c])
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] != 1 or visited[nr][nc] != 0:
            continue
        dfs(n, nr, nc)


def connect(length, r, c, direction, start, goal):
    if arr[r][c] == goal:
        if length > 1:
            graph[start][goal] = min(graph[start][goal], length)
            graph[goal][start] = min(graph[goal][start], length)
        return
    delta = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
    nr, nc = delta[direction]
    if 0 <= nr < N and 0 <= nc < M:
        if arr[nr][nc] == 0 or arr[nr][nc] == goal:
            connect(length+1, nr, nc, direction, start, goal)


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x, y = find(x), find(y)
    parents[max(x, y)] = min(x, y)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
islands = [[]]

# 섬 번호 붙이기
n = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            islands.append([])
            dfs(n, i, j)
            n += 1

# 섬 연결하기
inf = int(1e9)
graph = [[inf]*n for _ in range(n)]
for i in range(1, n-1):
    for j in range(i+1, n):
        #  i번 섬에서 j번 섬까지 연결
        for x, y in islands[i]:
            delta = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
            for k in range(4):
                nx, ny = delta[k]
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                    connect(0, nx, ny, k, i, j)

bridges = []
for i in range(1, n-1):
    for j in range(i+1, n):
        if graph[i][j] != inf:
            bridges.append([i, j, graph[i][j]])
bridges.sort(key=lambda x:x[2])

ans, cnt = 0, 0
parents = [i for i in range(n)]
for x, y, length in bridges:
    if find(x) != find(y):
        union(x, y)
        ans += length
        cnt += 1
if ans == 0 or cnt != n-2:
    print(-1)
else:
    print(ans)
