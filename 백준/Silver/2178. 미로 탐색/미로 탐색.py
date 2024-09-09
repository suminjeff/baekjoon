import sys


def solve_bfs(n, m, maze):
    from collections import deque

    visited = [[sys.maxsize]*m for _ in range(n)]
    visited[0][0] = 1
    que = deque([[0, 0]])

    while que:
        r, c = que.popleft()
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == '1' and visited[nr][nc] > visited[r][c]+1:
                visited[nr][nc] = visited[r][c]+1
                que.append([nr, nc])
    return visited[n-1][m-1]


if __name__ == '__main__':
    N, M = map(int, input().split())
    MAZE = [input() for _ in range(N)]
    ANSWER = solve_bfs(N, M, MAZE)
    print(ANSWER)