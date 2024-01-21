import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
arr = [input().rstrip() for _ in range(N)]
inf = sys.maxsize
distance = [[inf]*M for _ in range(N)]
distance[x1][y1] = 0
heap = [[0, x1, y1]]
while heap:
    n, x, y = heappop(heap)
    if distance[x][y] < n:
        continue
    if x == x2 and y == y2:
        break
    for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
        if 0 <= nx < N and 0 <= ny < M:
            nn = n
            if arr[nx][ny] == '1':
                nn += 1
            if distance[nx][ny] > nn:
                distance[nx][ny] = nn
                heappush(heap, [nn, nx, ny])
print(distance[x2][y2]+1)