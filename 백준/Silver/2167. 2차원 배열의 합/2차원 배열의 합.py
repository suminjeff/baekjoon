N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
for k in range(K):
    i, j, x, y = map(int, input().split())
    ans = 0
    for row in range(i-1, x):
        for col in range(j-1, y):
            ans += arr[row][col]
    print(ans)