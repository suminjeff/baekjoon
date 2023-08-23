C, R = map(int, input().split())
K = int(input())

if K > C * R:
    ans = 0
    print(ans)

else:
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    arr = [[0] * C for _ in range(R)]
    n = 1
    r = c = k = 0
    ans_r = 0
    ans_c = 0

    while n <= R * C:
        if 0 <= r < R and 0 <= c < C and arr[r][c] == 0:
            arr[r][c] = n
            if n == K:
                ans_r = r+1
                ans_c = c+1
                break
            n += 1
            r += dr[k]
            c += dc[k]
        else:
            r -= dr[k]
            c -= dc[k]
            k = (k + 1) % 4
            r += dr[k]
            c += dc[k]
    print(ans_c, ans_r)