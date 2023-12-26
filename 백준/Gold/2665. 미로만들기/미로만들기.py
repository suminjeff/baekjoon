import sys
input = sys.stdin.readline

from heapq import heappop, heappush

inf = int(1e9)
N = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
distance = [[inf]*N for _ in range(N)]
distance[0][0] = 0
heap = []
heappush(heap, [0, 0, 0])
while heap:
    b, r, c = heappop(heap)
    if r == c == N-1:
        print(distance[r][c])
        break
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0:
                nb = b+1
            else:
                nb = b
            if nb < distance[nr][nc]:
                distance[nr][nc] = nb
                heappush(heap, [nb, nr, nc])

