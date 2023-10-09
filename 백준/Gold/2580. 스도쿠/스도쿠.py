import sys
input = sys.stdin.readline


def get_blanks():
    res = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                res.append([i, j])
    return res


def backtrack(idx):
    if idx == len(blanks):
        for i in range(9):
            print(*board[i])
        exit()
    r, c = blanks[idx]
    for n in get_possible_numbers(r, c):
        board[r][c] = n
        backtrack(idx+1)
        board[r][c] = 0





def get_possible_numbers(r, c):
    row_counts = [0]*10
    col_counts = [0]*10
    box_counts = [0]*10
    for i in range(9):
        row_counts[board[i][c]] += 1
        col_counts[board[r][i]] += 1
    for n in range(0, 9, 3):
        for m in range(0, 9, 3):
            if n <= r < n+3 and m <= c < m+3:
                for i in range(n, n+3):
                    for j in range(m, m+3):
                        box_counts[board[i][j]] += 1
    res = []
    for c in range(1, 10):
        if row_counts[c] == 0 and col_counts[c] == 0 and box_counts[c] == 0:
            res.append(c)
    return res


board = [list(map(int, input().split())) for _ in range(9)]
blanks = get_blanks()
backtrack(0)