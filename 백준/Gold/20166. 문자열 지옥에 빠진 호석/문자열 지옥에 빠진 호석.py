from collections import deque


def bfs(row, col):
    que = deque()
    que.append([row, col, arr[row][col]])

    while que:
        r, c, s = que.popleft()
        if s not in string_dict:
            string_dict.setdefault(s, 0)
        string_dict[s] += 1

        if len(s) >= 5:
            continue

        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1], [r+1, c+1], [r+1, c-1], [r-1, c+1], [r-1, c-1]]:
            if nr == N:
                nr = 0
            elif nr == -1:
                nr = N-1
            if nc == M:
                nc = 0
            elif nc == -1:
                nc = M-1
            que.append([nr, nc, s+arr[nr][nc]])


N, M, K = map(int, input().split())
arr = [list(input()) for _ in range(N)]

string_dict = {}

answer = []

for i in range(N):
    for j in range(M):
        bfs(i, j)

for _ in range(K):
    string = input()
    if string in string_dict:
        print(string_dict[string])
    else:
        print(0)
