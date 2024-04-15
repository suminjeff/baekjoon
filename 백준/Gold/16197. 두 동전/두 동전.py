import sys
from collections import deque


# 16197

def bfs(que):
    while que:
        cnt, coin1, coin2 = que.popleft()
        x1, y1 = coin1
        x2, y2 = coin2

        if cnt >= 10:
            return -1

        for d in range(4):
            dx, dy = delta[d]
            nx1, ny1 = x1+dx, y1+dy
            nx2, ny2 = x2+dx, y2+dy

            if (0 <= nx1 < N and 0 <= ny1 < M) and (0 <= nx2 < N and 0 <= ny2 < M):
                if arr[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if arr[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                que.append([cnt+1, [nx1, ny1], [nx2, ny2]])
            else:
                if (0 <= nx1 < N and 0 <= ny1 < M) or (0 <= nx2 < N and 0 <= ny2 < M):
                    return cnt+1


delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

coins = [0]
for i in range(N):
    for j in range(M):
        v = arr[i][j]
        if v == 'o':
            coins.append([i, j])
que = deque([coins])

print(bfs(que))