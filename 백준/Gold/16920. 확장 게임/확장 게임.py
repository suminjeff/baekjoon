import sys
input = sys.stdin.readline
from collections import deque

# 16920


def play(player):
    global T
    if not que_dict[player]:
        return
    for i in range(S[player]):
        que = que_dict[player]
        if not que:
            return 
        que_length = len(que)
        for j in range(que_length):
            r, c = que.popleft()
            T -= 1
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '.':
                    arr[nr][nc] = str(player)
                    que.append([nr, nc])
                    ans[player] += 1
                    T += 1


N, M, P = map(int, input().split())
S = [0]+list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(N)]

que_dict = {x:deque() for x in range(1, P+1)}
ans = [0]*(P+1)
T = 0

for i in range(N):
    for j in range(M):
        v = arr[i][j]
        if v.isnumeric():
            que_dict[int(v)].append([i, j])
            ans[int(v)] += 1
            T += 1

while T:
    for i in range(1, P+1):
        play(i)

print(*ans[1:])