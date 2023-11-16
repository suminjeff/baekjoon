import sys
input = sys.stdin.readline

from collections import deque

def dfs(p, r, c, depth):
    global ans
    if depth == 0:
        ans += p
        return
    if p == 0.0:
        return
    for i in range(4):
        dr, dc = delta[i]
        nr, nc = r+dr, c+dc
        if 0 <= nr < M and 0 <= nc < M and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(p*probability[i], nr, nc, depth-1)
            visited[nr][nc] = 0


N, east, west, south, north = map(int, input().split())
probability = [east/100, west/100, south/100, north/100]
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
M = 2*N+1
visited = [[0]*M for _ in range(M)]
visited[N][N] = 1
ans = 0
dfs(1, N, N, N)
print(ans)