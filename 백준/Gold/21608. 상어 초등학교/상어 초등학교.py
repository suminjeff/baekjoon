import sys
input = sys.stdin.readline


# 21608 상어 초등학교


N = int(input())
seats = [[0]*N for _ in range(N)]
empty = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            if 0 <= ni < N and 0 <= nj < N:
                empty[ni][nj] += 1
position = [[] for _ in range(N**2+1)]
shark_friends = {}
for _ in range(N**2):
    shark, *friends = map(int, input().split())
    shark_friends.setdefault(shark, friends)
    check = [[0]*N for _ in range(N)]
    possible = []
    for f in friends:
        if position[f]:
            i, j = position[f]
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= ni < N and 0 <= nj < N and seats[ni][nj] == 0:
                    check[ni][nj] += 1
                    possible.append([ni, nj, check[ni][nj], empty[ni][nj]])
    if not possible:
        for i in range(N):
            for j in range(N):
                if seats[i][j] == 0:
                    possible.append([i, j, check[i][j], empty[i][j]])
    possible.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
    x, y, c, e = possible[0]
    seats[x][y] = shark
    position[shark] = [x, y]
    for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
        if 0 <= nx < N and 0 <= ny < N and empty[nx][ny] > 0:
            empty[nx][ny] -= 1
score = {
    0: 0,
    1: 1,
    2: 10,
    3: 100,
    4: 1000,
}
ans = 0
for shark, friends in shark_friends.items():
    x, y = position[shark]
    tmp = 0
    for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
        if 0 <= nx < N and 0 <= ny < N and seats[nx][ny] in friends:
            tmp += 1
    ans += score[tmp]
print(ans)