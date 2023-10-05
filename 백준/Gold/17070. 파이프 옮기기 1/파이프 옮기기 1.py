pipe = {
    0: [[0, 1, 0], [1, 1, 2]],
    1: [[1, 0, 1], [1, 1, 2]],
    2: [[0, 1, 0], [1, 0, 1], [1, 1, 2]],
}

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = 0

# memo 배열 초기화
memo = [[[-1 for _ in range(3)] for _ in range(N)] for _ in range(N)]

def dfs(r, c, p, cnt, memo):
    if r == c == N-1:
        return 1

    if memo[r][c][p] != -1:
        return memo[r][c][p]

    total_cnt = 0

    for dr, dc, np in pipe[p]:
        nr, nc = r + dr, c + dc
        if np == 2:  # 'd' 대신 2를 사용
            if nr < N and nc < N and arr[nr][nc] == arr[nr-1][nc] == arr[nr][nc-1] == 0:
                total_cnt += dfs(nr, nc, np, 0, memo)
        else:
            if nr < N and nc < N and arr[nr][nc] == 0:
                total_cnt += dfs(nr, nc, np, 0, memo)

    memo[r][c][p] = total_cnt
    return total_cnt

# 시작 지점이 (0, 1)이고 시작 방향이 'h' (가로)인 상황에서 DFS 시작
result = dfs(0, 1, 0, 0, memo)
print(result)