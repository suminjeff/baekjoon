
def main():
    n, m = 5, 6
    arr = [list(map(int, input().split())) for _ in range(n)]
    log = set()

    def dfs(depth, number_string, r, c):
        if depth == m:
            log.add(number_string)
            return
        for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
            if 0 <= nr < n and 0 <= nc < n:
                nv = arr[nr][nc]
                dfs(depth + 1, number_string + str(nv), nr, nc)

    for i in range(n):
        for j in range(n):
            v = arr[i][j]
            dfs(1, str(v), i, j)

    print(len(log))


if __name__ == '__main__':
    main()
