def chessboard(board_type, r, c):
    global min_cnt
    cnt = 0
    sr, sc = r, c
    for row in range(r, r+8):
        for col in range(c, c+8):
            v, s = board[row][col], board_type[sr-row][sc-col]
            if v != s:
                cnt += 1
                if cnt >= min_cnt:
                    return cnt
    return cnt


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
cell = ['B', 'W']
row1 = []
row2 = []
i = 0
for _ in range(8):
    row1.append(cell[i])
    row2.append(cell[1-i])
    i = 1-i

board1 = []
board2 = []
for _ in range(4):
    board1.append(row1)
    board1.append(row2)
    board2.append(row2)
    board2.append(row1)

min_cnt = N*M
for r in range(N-8+1):
    for c in range(M-8+1):
        color = board[r][c]
        cnt1 = chessboard(board1, r, c)
        cnt2 = chessboard(board2, r, c)
        min_cnt = min(min_cnt, cnt1, cnt2)
print(min_cnt)