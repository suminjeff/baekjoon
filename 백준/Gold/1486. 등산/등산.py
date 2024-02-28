import sys
from heapq import heappop, heappush

# 1486

N, M, T, D = map(int, input().split())
arr = [list(input()) for _ in range(N)]
heap2 = []
for i in range(N):
    for j in range(M):
        v = arr[i][j]
        if v.isupper():
            n = ord(v)-65
        else:
            n = ord(v)-71
        arr[i][j] = n
        heappush(heap2, [-n, i, j])

inf = sys.maxsize
time1 = [[inf for _ in range(M)] for _ in range(N)]
time1[0][0] = 0
heap1 = [[0, 0, 0]]
res = []

while heap1:
    t, r, c = heappop(heap1)
    v = arr[r][c]
    res.append(v)
    if time1[r][c] < t or time1[r][c] > D:
        continue
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < M:
            nv = arr[nr][nc]
            if abs(v-nv) <= T:
                if v >= nv:
                    nt = t+1
                else:
                    nt = t+(v-nv)**2
                if time1[nr][nc] > nt:
                    time1[nr][nc] = nt
                    heappush(heap1, [nt, nr, nc])
while heap2:
    h, i, j = heappop(heap2)
    time2 = [[inf for _ in range(M)] for _ in range(N)]
    time2[i][j] = 0
    heap3 = [[0, i, j]]
    while heap3:
        t, r, c = heappop(heap3)
        v = arr[r][c]
        res.append(v)
        if time2[r][c] < t or time2[r][c] > D:
            continue
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < M:
                nv = arr[nr][nc]
                if abs(v-nv) <= T:
                    if v >= nv:
                        nt = t+1
                    else:
                        nt = t+(v-nv)**2
                    if time2[nr][nc] > nt:
                        time2[nr][nc] = nt
                        heappush(heap3, [nt, nr, nc])
    if time1[i][j] + time2[0][0] <= D:
        print(arr[i][j])
        break
