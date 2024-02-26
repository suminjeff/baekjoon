# 15684


def check():
    for c in range(N):
        k = c
        for r in range(H):
            if ladder[r][k] == 1:
                k += 1
            elif ladder[r][k-1] == 1:
                k -= 1
        if c != k:
            return False
    return True


def place(n, idx):
    global min_n
    if n >= min_n:
        return
    if check():
        min_n = min(min_n, n)
        return
    if n > 3:
        return
    for i in range(idx, K):
        r, c = candidates[i]
        if ladder[r][c-1] == ladder[r][c+1] == 0:
            ladder[r][c] = 1
            place(n+1, i+1)
            ladder[r][c] = 0


N, M, H = map(int, input().split())
ladder = [[0 for _ in range(N)] for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

candidates, K = [], 0
for i in range(H):
    for j in range(N-1):
        if ladder[i][j] == ladder[i][j-1] == ladder[i][j+1] == 0:
            candidates.append([i, j])
            K += 1
min_n = 4
place(0, 0)
print(min_n if min_n < 4 else -1)