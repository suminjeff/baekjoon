import sys


def solve(k, fold, hole):
    n = 2**k
    paper = [[0 for _ in range(n)] for _ in range(n)]
    sr, sc, er, ec = 0, 0, n-1, n-1
    for f in fold:
        hor, ver = ec-sc+1, er-sr+1
        if f == 'R':
            sc = sc+hor//2
        elif f == 'L':
            ec = ec-hor//2
        elif f == 'D':
            sr = sr+ver//2
        elif f == 'U':
            er = er-ver//2

    if sr != er or sc != ec:
        return 'IMPOSSIBLE'

    r, c = sr, sc
    for i in range(n):
        for j in range(n):
            # 같은 위치
            if abs(r-i) % 2 == 0 and abs(c-j) % 2 == 0:
                paper[i][j] = hole
            # 대각선
            elif abs(r-i) % 2 != 0 and abs(c-j) % 2 != 0:
                paper[i][j] = 3-hole
            # 가로 옆
            elif abs(r-i) % 2 == 0 and abs(c-j) % 2 != 0:
                paper[i][j] = 5-hole if hole in [2, 3] else 1-hole
            # 세로 옆
            elif abs(r-i) % 2 != 0 and abs(c-j) % 2 == 0:
                paper[i][j] = 2-hole if hole in [0, 2] else 4-hole
    return paper


if __name__ == '__main__':
    K = int(input())
    FOLD = list(input().split())
    HOLE = int(input())
    ANSWER = solve(K, FOLD, HOLE)
    for ROW in ANSWER:
        print(*ROW)