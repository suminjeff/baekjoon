import sys
input = sys.stdin.readline

from collections import deque


def find_S():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    return [i, j, k]


def find_E():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'E':
                    return [i, j, k]


while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    building = [[list(input().rstrip()) for _ in range(R+1)] for _ in range(L)]
    visited = [[[-1]*C for _ in range(R)] for _ in range(L)]
    sl, sr, sc = find_S()
    el, er, ec = find_E()
    visited[sl][sr][sc] = 0
    que = deque([[sl, sr, sc]])
    while que:
        l, r, c = que.popleft()
        if building[l][r][c] == 'E':
            break
        for nl, nr, nc in [[l, r+1, c], [l, r-1, c], [l, r, c+1], [l, r, c-1], [l+1, r, c], [l-1, r, c]]:
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and building[nl][nr][nc] != '#' and visited[nl][nr][nc] == -1:
                visited[nl][nr][nc] = visited[l][r][c] + 1
                que.append([nl, nr, nc])
    t = visited[el][er][ec]
    if t == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {t} minute(s).")