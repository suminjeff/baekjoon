import sys
from collections import deque
# 20058

N, Q = map(int, input().split())

# M: 2^N
M = 2**N
arr = [list(map(int, input().split())) for _ in range(M)]
L = list(map(int, input().split()))

# K: 얼음의 총량
K = 0
for i in range(M):
    for j in range(M):
        if arr[i][j] > 0:
            K += arr[i][j]


for q in range(Q):
    # m: 파이어스톰의 작은 범위
    m = 2**L[q]
    # 바뀐 0의 좌표들
    zeros = []
    for r in range(0, M, m):
        for c in range(0, M, m):
            # 큐에 행 증가, 열 증가 방향으로 담기
            que = deque()
            for p in range(r, r+m):
                for q in range(c, c+m):
                    que.append(arr[p][q])
            # 큐에서 열 감소, 행 증가 방향으로 뽑기
            for q in range(c+m-1, c-1, -1):
                for p in range(r, r+m):
                    v = que.popleft()
                    arr[p][q] = v
                    # 큐에서 뽑은 값이 0이라면 바뀐 0의 좌표들에 좌표값을 넣어줌
                    if v == 0:
                        zeros.append([p, q])
    # check: 인접한 얼음의 개수에 대한 정보
    check = [[2] + [3]*(M-2) + [2]] + [[3] + [4]*(M-2) + [3] for _ in range(M-2)] + [[2] + [3]*(M-2) + [2]]
    # melt: 녹을 예정인 얼음의 좌표
    melt = set()
    # 각 코너는 얼음이 있다면 무조건 녹을 예정 (인접한 칸이 최대 2개)
    for r, c in [[0, 0], [0, M-1], [M-1, 0], [M-1, M-1]]:
        if arr[r][c] > 0:
            melt.add((r, c))
    # 0의 좌표들 돌면서 인접한 칸 중에 얼음이 있으면 그 칸의 check값 -1 하면서 check값이 3 미만이 되면 set에 add
    for r, c in zeros:
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < M and 0 <= nc < M and arr[nr][nc] > 0:
                check[nr][nc] -= 1
                if check[nr][nc] < 3:
                    melt.add((nr, nc))
    # 녹을 예정인 좌표들의 얼음을 녹여주면서 K값도 같이 -1
    for r, c in melt:
        arr[r][c] -= 1
        K -= 1

# 마지막에는 bfs로 가장 큰 뭉치를 찾기
visited = [[0]*M for _ in range(M)]
max_cnt = 0
for i in range(M):
    for j in range(M):
        if arr[i][j] > 0 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 1
            que = deque([[i, j]])
            while que:
                r, c = que.popleft()
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < M and 0 <= nc < M and arr[nr][nc] > 0 and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        cnt += 1
                        que.append([nr, nc])
            max_cnt = max(max_cnt, cnt)
print(K)
print(max_cnt)

