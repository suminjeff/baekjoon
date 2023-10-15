import sys
input = sys.stdin.readline


def backtrack(depth, r, c, v):
    global max_v
    if depth == 4:
        if max_v < v:
            max_v = v
        return
    delta = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
    for nr, nc in delta:
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            backtrack(depth+1, nr, nc, v+arr[nr][nc])
            visited[nr][nc] = 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_v = 0
for i in range(N):
    for j in range(M):
        # 나머지 모양
        visited[i][j] = 1
        backtrack(1, i, j, arr[i][j])
        visited[i][j] = 0

        # ㅗ자 모양
        delta = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
        for k in range(4):
            v = arr[i][j]
            flag = True
            coor = [[i, j]]
            for nr, nc in delta:
                if delta[k] == [nr, nc]:
                    continue
                if 0 <= nr < N and 0 <= nc < M:
                    v += arr[nr][nc]
                    coor.append([nr, nc])
                else:
                    flag = False
                    break
            if flag:
                if max_v < v:
                    max_v = v
print(max_v)