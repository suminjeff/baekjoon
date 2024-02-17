import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 2151


def find_door():
    doors = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "#":
                doors.append([i, j])
    return doors


delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
reflect = [[2, 3], [2, 3], [0, 1], [0, 1]]

N = int(input())
arr = [input().rstrip() for _ in range(N)]
inf = sys.maxsize
mirrors = [[[inf]*4 for _ in range(N)] for _ in range(N)]

doors = find_door()
sx, sy = doors[0]
# 거울의 개수, 방향, 시직행, 시작열
heap = []
# 0: 왼쪽에서 오는, 1: 오른쪽에서 오는, 2: 위에서 오는, 3: 아래서 오는
for i in range(4):
    mirrors[sx][sy][i] = 0
    heappush(heap, [0, i, sx, sy])

while heap:
    m, d, r, c = heappop(heap)
    if mirrors[r][c][d] < m:
        continue

    # 거울 설치 불가능
    if arr[r][c] != "!":
        dr, dc = delta[d]
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != "*" and mirrors[nr][nc][d] > m:
            mirrors[nr][nc][d] = m
            heappush(heap, [m, d, nr, nc])
    # 거울 설치 가능
    elif arr[r][c] == "!":
        # 거울을 설치 x
        dr, dc = delta[d]
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != "*" and mirrors[nr][nc][d] > m:
            mirrors[nr][nc][d] = m
            heappush(heap, [m, d, nr, nc])
        # 거울을 설치 o
        nm = m+1
        for nd in reflect[d]:
            dr, dc = delta[nd]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != "*" and mirrors[nr][nc][nd] > nm:
                mirrors[nr][nc][nd] = nm
                heappush(heap, [nm, nd, nr, nc])

ex, ey = doors[1]
print(min(mirrors[ex][ey]))