def check(board):
    N = len(board)
    bingo = 0

    temp = 0
    for i in range(N):
        temp += board[i][i]
    if temp == 0:
        bingo += 1

    temp = 0
    for i in range(N):
        temp += board[i][N-1 - i]
    if temp == 0:
        bingo += 1

    for i in range(N):
        temp = 0
        for j in range(N):
            temp += board[i][j]
        if temp == 0:
            bingo += 1

    for i in range(N):
        temp = 0
        for j in range(N):
            temp += board[j][i]
        if temp == 0:
            bingo += 1
    return bingo


def bingo(board, call):
    count = 0
    for k in range(N**2):
        for i in range(N):
            for j in range(N):
                if call[k] == board[i][j]:
                    count += 1
                    board[i][j] = 0
                    bingo = check(board)
                    if bingo >= 3:
                        return count

N = 5
board = [list(map(int, input().split())) for _ in range(N)]
call = []
for _ in range(N):
    call.extend(list(map(int, input().split())))

print(bingo(board, call))
