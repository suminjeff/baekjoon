T = int(input())
for tc in range(1, T+1):
    N = int(input())
    center = N//2

    crop = [list(input()) for _ in range(N)]
    vstd = [[0]*N for _ in range(N)]

    ans = 0
    area = (N//2+1)**2 + (N//2)**2

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    ans += int(crop[center][center])
    area -= 1
    que = [[center, center]]
    vstd[center][center] = 1

    while area:
        r, c = que.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if not vstd[nr][nc]:
                    que.append([nr, nc])
                    ans += int(crop[nr][nc])
                    vstd[nr][nc] = 1
                    area -= 1

    print(f"#{tc} {ans}")