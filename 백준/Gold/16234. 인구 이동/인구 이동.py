import sys
input = sys.stdin.readline

from collections import deque


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
day = 0
while True:
    border = [[0]*N for _ in range(N)]
    population = {}
    group = 1
    flag = False
    for i in range(N):
        for j in range(N):
            if border[i][j] == 0:
                que = deque()
                que.append([i, j])
                population.setdefault(group, [1, arr[i][j]])
                border[i][j] = group
                while que:
                    r, c = que.popleft()
                    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                        if 0 <= nr < N and 0 <= nc < N and border[nr][nc] == 0:
                            if L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                                flag = True
                                population[group][0] += 1
                                population[group][1] += arr[nr][nc]
                                border[nr][nc] = group
                                que.append([nr, nc])
                group += 1
    if not flag:
        break
    for r in range(N):
        for c in range(N):
            k = border[r][c]
            n, p = population[k]
            np = p//n
            arr[r][c] = np
    day += 1
print(day)



