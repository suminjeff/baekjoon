T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for row in range(N):
        for col in range(N):
            kill = 0
            for r in range(M):
                for c in range(M):
                    kill_row = row + r
                    kill_col = col + c
                    if 0 <= kill_row < N and 0 <= kill_col < N:
                        kill += arr[kill_row][kill_col]
                        if max_kill < kill:
                            max_kill = kill

    print(f"#{tc} {max_kill}")