import sys

from collections import deque


def solve(n, m, r, a, command):
    for cmd in command:
        if cmd == 1:
            a = a[::-1]
        elif cmd == 2:
            for i in range(n):
                a[i] = a[i][::-1]
        elif cmd == 3:
            na = [[0]*n for _ in range(m)]
            stack = []
            for i in range(n):
                for j in range(m):
                    stack.append(a[i][j])
            for j in range(n):
                for i in range(m-1, -1, -1):
                    na[i][j] = stack.pop()
            a = na
            n, m = m, n
        elif cmd == 4:
            na = [[0]*n for _ in range(m)]
            stack = []
            for i in range(n):
                for j in range(m):
                    stack.append(a[i][j])
            for j in range(n-1, -1, -1):
                for i in range(m):
                    na[i][j] = stack.pop()
            a = na
            n, m = m, n
        elif cmd == 5:
            coordinates = deque([[0, 0], [0, m//2], [n//2, m//2], [n//2, 0]])
            que = deque()
            for i, j in coordinates:
                for r in range(i, i+n//2):
                    for c in range(j, j+m//2):
                        que.append(a[r][c])
            coordinates.rotate(-1)
            # 1 -> 2 -> 3 -> 4 -> 1
            for i, j in coordinates:
                for r in range(i, i+n//2):
                    for c in range(j, j+m//2):
                        a[r][c] = que.popleft()
        elif cmd == 6:
            coordinates = deque([[0, 0], [0, m//2], [n//2, m//2], [n//2, 0]])
            que = deque()
            for i, j in coordinates:
                for r in range(i, i+n//2):
                    for c in range(j, j+m//2):
                        que.append(a[r][c])
            coordinates.rotate(1)
            # 1 -> 2 -> 3 -> 4 -> 1
            for i, j in coordinates:
                for r in range(i, i+n//2):
                    for c in range(j, j+m//2):
                        a[r][c] = que.popleft()
    return a


if __name__ == '__main__':
    N, M, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    COMMAND = list(map(int, input().split()))
    ANSWER = solve(N, M, R, A, COMMAND)
    for ROW in ANSWER:
        print(*ROW)