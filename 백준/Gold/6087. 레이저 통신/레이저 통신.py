import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 6087

W, H = map(int, input().split())
arr = [input().rstrip() for _ in range(H)]
C = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == "C":
            C.append([i, j])
start, end = C
inf = sys.maxsize
visited = [[[inf]*4 for _ in range(W)] for _ in range(H)]
sr, sc = start
visited[sr][sc] = [0]*4
heap = []
for i in range(4):
    heappush(heap, [0]+[i]+start)

while heap:
    t, d, r, c = heappop(heap)
    if visited[r][c][d] < t:
        continue
    delta = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
    for nd in range(4):
        nr, nc = delta[nd]
        if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] != "*":
            if nd == d:
                if visited[nr][nc][nd] > visited[r][c][d]:
                    visited[nr][nc][nd] = visited[r][c][d]
                    heappush(heap, [t, nd, nr, nc])
            else:
                if visited[nr][nc][nd] > visited[r][c][d]+1:
                    visited[nr][nc][nd] = visited[r][c][d]+1
                    heappush(heap, [t+1, nd, nr, nc])
er, ec = end
print(min(visited[er][ec]))