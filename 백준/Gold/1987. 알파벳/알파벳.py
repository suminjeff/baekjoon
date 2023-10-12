import sys
input = sys.stdin.readline


def dfs(r, c, visited, depth):
    global max_depth
    max_depth = max(max_depth, depth)
    v = arr[r][c]
    visited[ord(v)-65] = 1
    delta = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
    for nr, nc in delta:
        if 0 <= nr < R and 0 <= nc < C:
            nv = arr[nr][nc]
            if visited[ord(nv)-65] == 0:
                dfs(nr, nc, visited, depth+1)
                visited[ord(nv)-65] = 0


visited = [0]*26
R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
max_depth = 0
dfs(0, 0, visited, 1)
print(max_depth)
