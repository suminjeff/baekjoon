import sys
input = sys.stdin.readline

from collections import deque


N, M = 12, 6
arr = [list(input().rstrip()) for _ in range(N)]


ans = 0
while True:

    # 뭉쳐있는 뿌요 확인
    visited = [[0]*M for _ in range(N)]
    puyos = []
    for i in range(N-1, -1, -1):
        for j in range(M):
            if arr[i][j].isalpha() and visited[i][j] == 0:
                cnt = 1
                color = arr[i][j]
                visited[i][j] = 1
                que = deque([[i, j]])
                cluster = [[i, j]]
                while que:
                    r, c = que.popleft()
                    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] == color:
                            visited[nr][nc] = 1
                            cnt += 1
                            cluster.append([nr, nc])
                            que.append([nr, nc])
                if cnt >= 4:
                    puyos.append(cluster)
    # 뿌요 터트리기
    if not puyos:
        break
    else:
        for puyo in puyos:
            for x, y in puyo:
                arr[x][y] = "."
    ans += 1
    # 뿌요 떨어지기
    for col in range(M):
        que = deque()
        for row in range(N-1, -1, -1):
            v = arr[row][col]
            if v.isalpha():
                arr[row][col] = "."
                que.append(v)
        r = N-1
        while que:
            arr[r][col] = que.popleft()
            r -= 1

print(ans)