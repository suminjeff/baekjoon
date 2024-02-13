from collections import deque
def solution(land):
    N, M = len(land), len(land[0])
    pipe = [0]*M
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and visited[i][j] == 0:
                columns = set()
                columns.add(j)
                size = 1
                visited[i][j] = 1
                que = deque([[i, j]])
                while que:
                    r, c = que.popleft()
                    for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                        if 0 <= nr < N and 0 <= nc < M and land[nr][nc] == 1 and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            size += 1
                            columns.add(nc)
                            que.append([nr, nc])
                for col in list(columns):
                    pipe[col] += size
    answer = max(pipe)
    return answer