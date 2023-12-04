import sys
input = sys.stdin.readline

from collections import deque

N, M, K = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
que = deque([[0, 0, 0]])
visited[0][0][0] = 1
ans = 0
while que:
    r, c, w = que.popleft()
    if (r, c) == (N-1, M-1):
        ans = visited[r][c][w]
        break
    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == '1' and w < K and visited[nr][nc][w+1] == 0:
                visited[nr][nc][w+1] = visited[r][c][w]+1
                que.append([nr, nc, w+1])
            elif arr[nr][nc] == '0' and visited[nr][nc][w] == 0:
                visited[nr][nc][w] = visited[r][c][w]+1
                que.append([nr, nc, w])
print(ans if ans > 0 else -1)