from sys import stdin

N = int(stdin.readline())

arr = [[0] * 1001 for _ in range(1001)]


max_row = 0
max_col = 0
for i in range(1, N+1):
    c, r, nr, nc = map(int, stdin.readline().split())
    if max_row < r + nr:
        max_row = r + nr
    if max_col < c + nc:
        max_col = c + nc

    for row in range(r, r+nr):
        for col in range(c, c+nc):
            arr[row][col] = i

for i in range(1, N+1):
    ans = 0
    for row in range(max_row):
        for col in range(max_col):
            if arr[row][col] == i:
                ans += 1
    print(ans)
