import sys
from collections import deque

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
# 0=북, 1=동, 2=남, 3=서
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[0]*M for _ in range(N)]
cnt = 0
que = deque()
que.append([r, c, d])

while que:
    r, c, d = que.popleft()
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if cleaned[r][c] == 0:
        cleaned[r][c] = 1
        cnt += 1

    flag = False
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            if cleaned[nr][nc] == 0:
                flag = True
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우 flag=False,
    if flag is False:
        # 2-1. 바라보는 방향을 유지한 채로 한칸 후진할 수 있다면 한칸 후진하고 1번으로 돌아간다.
        dr, dc = delta[d]
        nr, nc = r - dr, c - dc
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                que.append([nr, nc, d])
            # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우 flag=True,
    else:
        for _ in range(4):
            # 3-1. 반시계 방향으로 90도 회전한다.
            d = d-1 if d >= 1 else 3
            # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            dr, dc = delta[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and cleaned[nr][nc] == 0:
                que.append([nr, nc, d])
                break
print(cnt)
