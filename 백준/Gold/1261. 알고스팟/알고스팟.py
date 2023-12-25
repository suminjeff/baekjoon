import sys
input = sys.stdin.readline

from heapq import heappop, heappush

inf = int(1e9)
M, N = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = [[inf]*M for _ in range(N)]
ans[0][0] = 0
heap = []
heappush(heap, [0, 0, 0])

while heap:
    w, r, c = heappop(heap)
    if r == N-1 and c == M-1:
        print(ans[r][c])
        break

    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1:
                nw = w+1
            else:
                nw = w
            if nw < ans[nr][nc]:
                ans[nr][nc] = nw
                heappush(heap, [nw, nr, nc])
