import sys
from collections import deque
from heapq import heappush, heappop


# 20061

def solve(n, blocks, block_type):
    blocks = deque(blocks)
    grid = [[0 for _ in range(4)] for _ in range(6)]
    score = 0
    block_count = 0
    while blocks:
        t, x, y = blocks.popleft()
        x = 0
        while True:
            flag = True  # flag: 블록이 그리드 안에 들어갈 수 있는지

            for dx, dy in block_type[t]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= 6 or ny < 0 or ny >= 4 or grid[nx][ny]:
                    flag = False
                    break

            if flag:
                x += 1

            else:
                pop_que = []
                x -= 1
                for dx, dy in block_type[t]:
                    nx, ny = x + dx, y + dy
                    grid[nx][ny] = 1
                    block_count += 1
                    if sum(grid[nx]) == 4:
                        heappush(pop_que, nx)

                while pop_que:
                    idx = heappop(pop_que)
                    score += 1
                    block_count -= sum(grid[idx])
                    grid.pop(idx)
                    grid = [[0]*4] + grid
                    x += 1

                if x < 2:
                    for _ in range(2-x):
                        block_count -= sum(grid[-1])
                        grid.pop()
                        grid = [[0] * 4] + grid
                break
    return score, block_count


if __name__ == '__main__':
    GREEN_BLOCK_TYPE = {
        1: [[0, 0]],
        2: [[0, 0], [0, 1]],
        3: [[0, 0], [1, 0]],
    }

    BLUE_BLOCK_TYPE = {
        1: [[0, 0]],
        2: [[0, 0], [1, 0]],
        3: [[0, 0], [0, -1]],
    }

    N = int(input())
    GREEN_BLOCKS = [list(map(int, input().split())) for _ in range(N)]
    BLUE_BLOCKS = []
    for I in range(N):
        T, X, Y = GREEN_BLOCKS[I]
        BLUE_BLOCKS.append([T, Y, 3-X])
    GREEN_SCORE, GREEN_BLOCK_COUNT = solve(N, GREEN_BLOCKS, GREEN_BLOCK_TYPE)
    BLUE_SCORE, BLUE_BLOCK_COUNT = solve(N, BLUE_BLOCKS, BLUE_BLOCK_TYPE)
    ANSWER1 = GREEN_SCORE + BLUE_SCORE
    ANSWER2 = GREEN_BLOCK_COUNT + BLUE_BLOCK_COUNT
    print(ANSWER1)
    print(ANSWER2)