import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 1584

N = int(input())
K = 500

arr = [[0]*(K+1) for _ in range(K+1)]

# 위험한 구역의 정보 (1)
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            arr[x][y] = 1

# 죽음의 구역의 정보 (2)
M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            arr[x][y] = 2

inf = sys.maxsize
life = [[inf]*(K+1) for _ in range(K+1)]
life[0][0] = 0

# 감소된 생명, 행, 열
heap = [[0, 0, 0]]

while heap:
    h, r, c = heappop(heap)
    if r == c == 500:
        break
    if life[r][c] < h:
        continue
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < K+1 and 0 <= nc < K+1 and arr[nr][nc] != 2:
            nh = h
            if arr[nr][nc] == 1:
                nh = h+1
            if life[nr][nc] > nh:
                life[nr][nc] = nh
                heappush(heap, [nh, nr, nc])

ans = life[-1][-1]
print(ans if ans != inf else -1)