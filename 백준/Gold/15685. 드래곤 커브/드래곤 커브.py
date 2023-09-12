def dragon_curve(coors):
    res = []
    r, c = coors[-1]
    for i in range(len(coors)-2, -1, -1):
        p, q = coors[i]
        a, b = r-p, c-q
        nr, nc = r-b, c+a
        res.append([nr, nc])
    return res


N = int(input())
MAX_X = MAX_Y = 100
grid = [[0] * (MAX_X+1) for _ in range(MAX_Y+1)]
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]

dr = [0, 1, 1]
dc = [1, 1, 0]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    grid[y][x] = 1
    stack = [[y, x]]
    # 0=우, 1=상, 2=좌, 3=하
    for gen in range(g+1):
        if gen == 0:
            dy, dx = direction[d][0], direction[d][1]
            ny, nx = y+dy, x+dx
            grid[ny][nx] = 1
            stack.append([ny, nx])
        else:
            stack.extend(dragon_curve(stack))
    for r, c in stack:
        grid[r][c] = 1

    ans = 0
    for r in range(MAX_Y+1):
        for c in range(MAX_X+1):
            cnt = 0
            if grid[r][c] == 1:
                cnt += 1
                for k in range(3):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < MAX_Y+1 and 0 <= nc < MAX_X+1 and grid[nr][nc] == 1:
                        cnt += 1
                if cnt == 4:
                    ans += 1
print(ans)
