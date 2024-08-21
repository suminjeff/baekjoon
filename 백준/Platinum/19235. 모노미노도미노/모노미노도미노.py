import sys

from collections import deque, defaultdict


class Game:
    block_type = {
        1: [[0, 0]],
        2: [[0, 0], [0, 1]],
        3: [[0, 0], [1, 0]]
    }

    def __init__(self):
        self.grid_row = 6
        self.grid_col = 4
        self.grid = [[0]*4 for _ in range(6)]
        self.block_pk = 1
        self.boom_stack = []
        self.overflow = []
        self.block_table = defaultdict(list)
        self.points = 0

    def boom(self):
        grid = self.grid
        stack = self.boom_stack
        stack.sort(reverse=True)
        boom_size = len(stack)
        self.points += boom_size
        R, C = self.grid_row, self.grid_col
        block_table = self.block_table
        while stack:
            r = stack.pop()
            for i in range(r):
                for c in range(C):
                    pk = grid[i][c]
                    if pk == 0:
                        continue
                    idx = block_table[pk].index([i, c])
                    block_table[pk][idx][0] += 1
            for c in range(C):
                pk = grid[r][c]
                if pk == 0:
                    continue
                block_table[pk].remove([r, c])
                if len(block_table[pk]) == 0:
                    block_table.pop(pk)
            grid.pop(r)
            grid.insert(0, [0]*C)

    def squash(self, r):
        R, C = self.grid_row, self.grid_col
        grid = self.grid
        block_table = self.block_table
        squash_size = 2-r
        for i in range(R-squash_size, R):
            for j in range(C):
                pk = grid[i][j]
                if pk == 0:
                    continue
                block_table[pk].remove([i, j])
                if not block_table[pk]:
                    block_table.pop(pk)
        for _ in range(squash_size):
            grid.insert(0, [0]*C)
            grid.pop()
        for pk in block_table.keys():
            for i in range(len(block_table[pk])):
                block_table[pk][i][0] += squash_size

    def place_block(self, t, r, c):
        grid = self.grid
        block_type = self.block_type
        pk = self.block_pk
        block_table = self.block_table
        for dr, dc in block_type[t]:
            nr, nc = r+dr, c+dc
            grid[nr][nc] = pk
            if grid[nr].count(0) == 0:
                self.boom_stack.append(nr)
            block_table[pk].append([nr, nc])
        self.block_pk += 1

    def get_next_row(self, t, c):
        grid = self.grid
        block_type = self.block_type
        for r in range(6):
            for dr, dc in block_type[t]:
                nr, nc = r+dr, c+dc
                if nr >= 6 or grid[nr][nc] != 0:
                    return r-1
        return 5

    def gravity(self):
        grid = self.grid
        block_table = self.block_table
        R = self.grid_row
        for pk, coordinates in block_table.items():
            min_fall = R
            for r, c in coordinates:
                same_pk = False
                fall = 0
                for nr in range(r+1, R):
                    if grid[nr][c] == pk:
                        same_pk = True
                        break
                    elif grid[nr][c] == 0:
                        fall += 1
                    else:
                        break
                if same_pk:
                    continue
                min_fall = min(min_fall, fall)

            for i in range(len(block_table[pk])):
                r, c = block_table[pk][i]
                grid[r][c] = 0
                block_table[pk][i][0] += min_fall
                nr = r+min_fall
                grid[nr][c] = pk
                if grid[nr].count(0) == 0:
                    if nr not in self.boom_stack:
                        self.boom_stack.append(nr)

    def play(self, blocks):
        blocks = deque(blocks)
        while blocks:
            t, r, c = blocks.popleft()
            nr = self.get_next_row(t, c)  # 블록이 위치할 행 찾기
            self.place_block(t, nr, c)  # 찾은 행에 블록 위치시키기
            # 터질 행이 있으면 터트리기
            while self.boom_stack:
                self.boom()
                self.gravity()
            # 만약 연한 블럭에 블럭이 있으면 밀어주기
            squash_row = -1
            for i in range(2):
                if self.grid[i].count(0) != 4:
                    squash_row = i
                    break
            if squash_row != -1:
                self.squash(squash_row)


if __name__ == '__main__':
    N = int(input())
    green_blocks = [list(map(int, input().split())) for _ in range(N)]
    blue_blocks = [[t if t == 1 else 5-t, y, 4-1-x if t != 3 else 4-1-x-1] for t, x, y in green_blocks]
    # green
    green_game = Game()
    green_game.play(green_blocks)
    remaining_green_blocks = sum([len(v) for v in green_game.block_table.values()])
    # blue
    blue_game = Game()
    blue_game.play(blue_blocks)
    remaining_blue_blocks = sum([len(v) for v in blue_game.block_table.values()])

    total_points = green_game.points + blue_game.points
    remaining_blocks = remaining_green_blocks + remaining_blue_blocks

    print(total_points)
    print(remaining_blocks)