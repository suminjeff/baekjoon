import sys
input = sys.stdin.readline
from collections import deque


def visit(x, y, visited):
    visited[x][y] = 1
    que = deque()
    que.append([x, y])
    while que:
        r, c = que.popleft()
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < M and arr[r][c] and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append([nr, nc])
    return visited


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 빙산의 개수 K
K = 0
water = [[0]*M for _ in range(N)]
ice = deque()
for i in range(N):
    for j in range(M):
        v = arr[i][j]
        if v > 0:
            K += 1
            ice.append([i, j, v])
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                    water[i][j] += 1


year = 0
is_connected = 1
# 빙산의 개수(K)가 모두 없어질 때까지
while K:
    # 빙산이 끊겨 있는지 확인
    visited = visit(ice[0][0], ice[0][1], [[0]*M for _ in range(N)])
    for k in range(K):
        vr, vc = ice[k][0], ice[k][1]
        if visited[vr][vc] == 0:
            is_connected = 0
            break
    if is_connected == 0:
        break
    # 안끊겨 있으면 진행
    melted = []
    # ice 돌면서 녹이기
    for _ in range(K):
        r, c, v = ice.popleft()
        nv = arr[r][c] - water[r][c]
        arr[r][c] = nv if nv > 0 else 0
        if nv > 0:
            ice.append([r, c, nv])
        else:
            K -= 1
            melted.append([r, c])
    # melted 돌면서 water 업데이트
    for r, c in melted:
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] > 0:
                water[nr][nc] += 1
    year += 1
    if K == 0:
        break
if is_connected == 1:
    print(0)
else:
    print(year)