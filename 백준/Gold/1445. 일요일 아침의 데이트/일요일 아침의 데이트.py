import sys
from heapq import heappop, heappush

# 1445

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
heap = []
fx, fy = -1, -1
for i in range(N):
    for j in range(M):
        v = arr[i][j]
        if v == "g":
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == ".":
                    arr[ni][nj] = "n"
        elif v == "S":
            heappush(heap, [0, 0, i, j])
        elif v == "F":
            fx, fy = i, j


INF = sys.maxsize
garbage = [[[INF] for _ in range(2)]*M for _ in range(N)]
ans1 = ans2 = 0
while heap:
    g, n, r, c = heappop(heap)
    if garbage[r][c][0] < g:
        continue
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < M:
            v = arr[nr][nc]
            ng, nn = g, n
            if v == "g":
                ng += 1
            elif v == "n":
                nn += 1
            if garbage[nr][nc][0] > ng:
                garbage[nr][nc] = [ng, nn]
                heappush(heap, [ng, nn, nr, nc])

print(*garbage[fx][fy])