T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            temp = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    if 0 <= r < N and 0 <= c < N:
                        temp += arr[r][c]
            if max_v < temp:
                max_v = temp
    print(f"#{tc} {max_v}")