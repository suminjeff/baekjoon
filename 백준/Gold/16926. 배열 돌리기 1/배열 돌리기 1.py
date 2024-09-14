import sys


def turn(n, m, r, a):
    na = [[0]*m for i in range(n)]

    for i in range(min(n, m)//2):
        stack = []

        r = c = i

        # 아래
        while r < n-i:
            stack.append(a[r][c])
            r += 1
        r -= 1
        c += 1

        # 오른쪽
        while c < m-i:
            stack.append(a[r][c])
            c += 1
        c -= 1
        r -= 1

        # 위쪽
        while r >= i:
            stack.append(a[r][c])
            r -= 1
        r += 1
        c -= 1

        # 왼쪽
        while c > i:
            stack.append(a[r][c])
            c -= 1

        # === 뿌리기 ===

        r = c = i

        # 오른쪽
        while c < m-i:
            na[r][c] = stack.pop()
            c += 1
        c -= 1
        r += 1

        # 아래
        while r < n-i:
            na[r][c] = stack.pop()
            r += 1
        r -= 1
        c -= 1

        # 왼쪽
        while c >= i:
            na[r][c] = stack.pop()
            c -= 1
        c += 1
        r -= 1

        # 위쪽
        while r > i:
            na[r][c] = stack.pop()
            r -= 1

    return na


def solve(n, m, r, a):
    for _ in range(r):
        a = turn(n, m, r, a)
    return a



if __name__ == '__main__':
    N, M, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ANSWER = solve(N, M, R, A)
    for ROW in ANSWER:
        print(*ROW)