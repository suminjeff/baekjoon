import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations


def can_continue(enemy):
    for i in range(N):
        for j in range(M):
            if enemy[i][j] == 1:
                return True
    return False


def shoot(archer_position):
    clone = [row[:] for row in enemy]
    kill_cnt = 0
    if can_continue(clone):
        killed = [[0]*M for _ in range(N)]
        for i in range(N-1, -1, -1):
            targets = []
            for j in archer_position:
                que = deque()
                que.append([i, j, 1])
                while que:
                    r, c, d = que.popleft()
                    if clone[r][c] == 1:
                        targets.append([r, c])
                        if killed[r][c] == 0:
                            killed[r][c] = 1
                            kill_cnt += 1
                        break
                    if d < D:
                        for dr, dc in shooting_direction:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < N and 0 <= nc < M:
                                que.append([nr, nc, d+1])
            for p, q in targets:
                clone[p][q] = 0
    return kill_cnt


shooting_direction = [[0, -1], [-1, 0], [0, 1]]
N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]
position = [m for m in range(M)]
max_cnt = 0

for archer_position in combinations(position, 3):
    cnt = shoot(archer_position)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)