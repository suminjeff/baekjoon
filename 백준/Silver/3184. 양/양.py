import sys
input = sys.stdin.readline
from collections import deque

# 3184

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
sheep, wolf = 0, 0

for i in range(R):
    for j in range(C):
        if arr[i][j] == "o":
            sheep += 1
        elif arr[i][j] == "v":
            wolf += 1

for i in range(R):
    for j in range(C):
        if arr[i][j] != "#" and visited[i][j] == 0:
            visited[i][j] = 1
            sheep_cnt, wolf_cnt = 0, 0
            if arr[i][j] == "o":
                sheep_cnt += 1
            elif arr[i][j] == "v":
                wolf_cnt += 1
            que = deque([[i, j]])
            while que:
                r, c = que.popleft()
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != "#" and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        if arr[nr][nc] == "o":
                            sheep_cnt += 1
                        elif arr[nr][nc] == "v":
                            wolf_cnt += 1
                        que.append([nr, nc])
            if sheep_cnt and wolf_cnt:
                if sheep_cnt > wolf_cnt:
                    wolf -= wolf_cnt
                else:
                    sheep -= sheep_cnt
print(sheep, wolf)