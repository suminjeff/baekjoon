T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    t_nr = [0, 1, 0, -1]
    t_nc = [1, 0, -1, 0]
    t_kill = 0

    x_nr = [1, 1, -1, -1]
    x_nc = [1, -1, -1, 1]
    x_kill = 0

    for r in range(N):
        for c in range(N):
            t_temp = arr[r][c]
            x_temp = arr[r][c]
            for m in range(1, M):
                for t in range(4):
                    tr = r + t_nr[t] * m
                    tc = c + t_nc[t] * m
                    if 0 <= tr < N and 0 <= tc < N:
                        t_temp += arr[tr][tc]
                for x in range(4):
                    xr = r + x_nr[x] * m
                    xc = c + x_nc[x] * m
                    if 0 <= xr < N and 0 <= xc < N:
                        x_temp += arr[xr][xc]
            t_kill = max(t_kill, t_temp)
            x_kill = max(x_kill, x_temp)
    ans = max(t_kill, x_kill)
    print(f"#{test_case} {ans}")