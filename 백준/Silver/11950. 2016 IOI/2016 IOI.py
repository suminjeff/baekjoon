T = 1
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = []
    for k in range(1, N-1):
        for m in range(1, N-k):
            # print(k, m, k+m)
            white = blue = red = 0
            for w in range(k):
                for t in range(M):
                    if arr[w][t] != "W":
                        white += 1
            for b in range(k, k+m):
                for u in range(M):
                    if arr[b][u] != "B":
                        blue += 1
            for r in range(k+m, N):
                for d in range(M):
                    if arr[r][d] != "R":
                        red += 1
            ans.append(white + blue + red)
    print(min(ans))