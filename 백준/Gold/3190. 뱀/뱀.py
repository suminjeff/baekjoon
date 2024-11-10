import sys

from collections import deque


def solve(n, k, apple, l, direction):
    board = [[0]*n for _ in range(n)]
    for i in range(k):
        r, c = apple[i]
        board[r-1][c-1] = 1

    board[0][0] = 2
    snake = deque([[0, 0]])

    idx = 0
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우, 하, 좌, 상

    current_time = 0
    for i in range(l):
        time, d = direction[i]
        r, c = snake[0]
        dr, dc = delta[idx]
        for t in range(current_time, time):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] <= 1:
                if board[nr][nc] == 0:
                    if snake:
                        tr, tc = snake.pop()
                        board[tr][tc] = 0
                    else:
                        snake.popleft()
                        board[r][c] = 0
                board[nr][nc] = 2
                snake.appendleft([nr, nc])
                r, c = nr, nc
            else:
                return t+1

        if d == "L":
            idx = (idx + 3) % 4
        else:
            idx = (idx + 1) % 4
        current_time = time

    dr, dc = delta[idx]

    while True:
        r, c = snake[0]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] <= 1:
            if board[nr][nc] == 0:
                if snake:
                    tr, tc = snake.pop()
                    board[tr][tc] = 0
                else:
                    snake.popleft()
                    board[r][c] = 0
            board[nr][nc] = 2
            snake.appendleft([nr, nc])
            r, c = nr, nc
            current_time += 1
        else:
            return current_time + 1


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    APPLE = [list(map(int, input().split())) for _ in range(K)]
    L = int(input())
    DIRECTION = [list(map(lambda x: int(x) if x.isnumeric() else x, input().split())) for _ in range(L)]
    ANSWER = solve(N, K, APPLE, L, DIRECTION)
    print(ANSWER)