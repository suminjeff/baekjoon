import sys


def solve(n, m, t, grid):
    from collections import deque
    # 0: 그람x, 1: 그람o
    visited = [[[sys.maxsize]*m for _ in range(n)] for _ in range(2)]
    visited[0][0][0] = 0
    start = [0, 0, 0]
    que = deque([start])
    while que:
        r, c, g = que.popleft()
        if g == 0:
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 1:
                    ng = int(grid[nr][nc] == 2)
                    if visited[ng][nr][nc] > visited[g][r][c] + 1:
                        visited[ng][nr][nc] = visited[g][r][c] + 1
                        que.append([nr, nc, ng])
        else:
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if 0 <= nr < n and 0 <= nc < m:
                    if visited[g][nr][nc] > visited[g][r][c] + 1:
                        visited[g][nr][nc] = visited[g][r][c] + 1
                        que.append([nr, nc, g])

    answer = min(visited[0][n-1][m-1], visited[1][n-1][m-1])

    return answer if answer <= t else "Fail"


if __name__ == '__main__':
    N, M, T = map(int, input().split())
    GRID = [list(map(int, input().split())) for _ in range(N)]
    ANSWER = solve(N, M, T, GRID)
    print(ANSWER)