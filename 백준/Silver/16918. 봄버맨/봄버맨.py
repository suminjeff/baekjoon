import sys


def solve(r, c, n, grid):

    bomb_time = [[-1]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                bomb_time[i][j] = 0
    t = 1
    while True:
        if t == n:
            break

        # 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
        t += 1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '.':
                    grid[i][j] = 'O'
                    bomb_time[i][j] = t
        if t == n:
            break

        # 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
        t += 1
        boom = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O' and bomb_time[i][j] == t-3:
                    boom.add((i, j))
                    for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                        if 0 <= ni < r and 0 <= nj < c:
                            boom.add((ni, nj))
        for x, y in boom:
            grid[x][y] = '.'
        if t == n:
            break

    return grid



if __name__ == '__main__':
    R, C, N = map(int, input().split())
    GRID = [list(input()) for _ in range(R)]
    ANSWER = solve(R, C, N, GRID)
    for ROW in ANSWER:
        print(*ROW, sep='')