import sys
input = sys.stdin.readline


def pruning(n):
    for i in range(n):
        if row[n] == row[i] or abs(row[n] - row[i]) == abs(n-i):
            return False
    return True


def n_queen(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for i in range(N):
        row[n] = i
        if pruning(n):
            n_queen(n+1)


N = int(input())
row = [0]*N
cnt = 0
n_queen(0)
print(cnt)