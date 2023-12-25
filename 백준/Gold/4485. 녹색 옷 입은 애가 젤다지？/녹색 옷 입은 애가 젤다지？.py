import sys
input = sys.stdin.readline

from heapq import heappop, heappush

tc = 1
inf = int(1e9)
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    heap = []
    heappush(heap, [arr[0][0], 0, 0])
    ans = [[inf]*N for _ in range(N)]
    ans[0][0] = 0
    while heap:
        v, r, c = heappop(heap)
        if r == c == N-1:
            print(f"Problem {tc}: {ans[r][c]}")
            break
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < N and v + arr[nr][nc] < ans[nr][nc]:
                nv = v + arr[nr][nc]
                ans[nr][nc] = nv
                heappush(heap, [nv, nr, nc])
    tc += 1