import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 22116

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
inf = sys.maxsize
res = [[sys.maxsize]*N for _ in range(N)]
res[0][0] = 0
# 경로상의 최대 경사, 행, 열
heap = [[0, 0, 0]]
while heap:
    m, r, c = heappop(heap)
    if res[r][c] < m:
        continue
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < N:
            k = abs(arr[r][c] - arr[nr][nc])
            nm = max(m, k)
            if res[nr][nc] > nm:
                res[nr][nc] = nm
                heappush(heap, [nm, nr, nc])
print(res[-1][-1])