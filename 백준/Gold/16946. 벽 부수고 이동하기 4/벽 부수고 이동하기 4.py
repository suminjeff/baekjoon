import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]

group = {}

# 0 덩어리 그룹화
g = 2
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            que = deque([[i, j]])
            arr[i][j] = g
            group.setdefault(g, 1)
            while que:
                r, c = que.popleft()
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] != 0:
                        continue
                    arr[nr][nc] = g
                    group[g] += 1
                    que.append([nr, nc])
            g += 1

ans = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] != 1:
            continue

        visited_group = {}
        count = 1
        for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] == 1 or visited_group.get(arr[ni][nj], 0):
                continue
            visited_group[arr[ni][nj]] = 1
            count += group[arr[ni][nj]]
        ans[i][j] = count % 10
for i in range(N):
    print(*ans[i], sep='')