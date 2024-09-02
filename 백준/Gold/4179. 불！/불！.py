import sys
from collections import deque


def solve(r, c, maze):

    jh_que = deque()
    jh_visited = [[-1 for _ in range(c)] for _ in range(r)]

    f_que = deque()
    f_visited = [[-1 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            v = maze[i][j]
            if v == 'J':
                jh_que.append([i, j])
                jh_visited[i][j] = 0
            elif v == 'F':
                f_que.append([i, j])
                f_visited[i][j] = 0

    while f_que:
        x, y = f_que.popleft()
        for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] in '.J' and f_visited[nx][ny] == -1:
                f_visited[nx][ny] = f_visited[x][y] + 1
                f_que.append([nx, ny])
    while jh_que:
        x, y = jh_que.popleft()
        if x == 0 or x == r-1 or y == 0 or y == c-1:
            return jh_visited[x][y]+1

        for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] in '.J' and jh_visited[nx][ny] == -1:
                nv = jh_visited[x][y]+1
                if f_visited[nx][ny] == -1 or f_visited[nx][ny] > nv:
                    jh_visited[nx][ny] = nv
                    jh_que.append([nx, ny])

    return 'IMPOSSIBLE'


if __name__ == '__main__':
    R, C = map(int, input().split())
    MAZE = [list(input()) for _ in range(R)]
    ANSWER = solve(R, C, MAZE)
    print(ANSWER)