import sys
input = sys.stdin.readline
from collections import deque

# 18405


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

virus = {}
que = []
for i in range(N):
    for j in range(N):
        v = arr[i][j]
        if v > 0:
            que.append([0, v, i, j])
            if v not in virus.keys():
                virus.setdefault(v, [])
            virus[v].append([i, j])
que.sort(key=lambda x:x[1])
que = deque(que)
while que:
    t, v, r, c = que.popleft()
    if t > S:
        break
    nt = t+1
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            if nt <= S:
                arr[nr][nc] = v
                que.append([nt, v, nr, nc])

print(arr[X-1][Y-1])