import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def f(r, c):
    if c == C-1:
        return True
    for nr, nc in [[r-1, c+1], [r, c+1], [r+1, c+1]]:
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != 'x' and arr[nr][nc] != 'o':
            arr[nr][nc] = 'o'
            if f(nr, nc):
                return True
    return False


R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
ans = 0
for i in range(R):
    arr[i][0] = 'o'
    if f(i, 0):
        ans += 1
print(ans)