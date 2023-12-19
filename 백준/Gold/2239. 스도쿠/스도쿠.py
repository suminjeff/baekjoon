import sys
input = sys.stdin.readline


N = 9
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]

M = 0
zeros = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            M += 1
            zeros.append([i, j])


def backtrack(idx):
    if idx == M:
        for i in range(N):
            print(*arr[i], sep='')
        exit(0)
    r, c = zeros[idx]
    for n in range(1, 10):
        if is_valid(r, c, n):
            arr[r][c] = n
            backtrack(idx+1)
            arr[r][c] = 0


def is_valid(r, c, n):
    for k in range(N):
        if arr[r][k] == n:
            return False
        if arr[k][c] == n:
            return False
    boxr, boxc = (r//3)*3, (c//3)*3
    for nr in range(boxr, boxr+3):
        for nc in range(boxc, boxc+3):
            if arr[nr][nc] == n:
                return False
    return True


backtrack(0)