import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque


# 16985


def spin(height, plate):
    new_plate = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_plate[i][j] = plate[4-j][i]
    return new_plate


def permutation(n, r, k, perm, used):
    if r == k:
        plate_order.append(perm[:])
        return
    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            perm.append(i)
            permutation(n, r, k+1, perm, used)
            perm.pop()
            used[i] = 0


def product(n, r, k, prod):
    if r == k:
        spin_order.append(prod[:])
        return
    for i in range(n):
        prod.append(i)
        product(n, r, k+1, prod)
        prod.pop()


def bfs(arr):
    if arr[0][0][0] == 0 or arr[-1][-1][-1] == 0:
        return inf

    visited = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0
    que = deque([[0, 0, 0]])
    while que:
        h, r, c = que.popleft()
        for nh, nr, nc in [[h, r+1, c], [h, r-1, c], [h, r, c+1], [h, r, c-1], [h+1, r, c], [h-1, r, c]]:
            if 0 <= nh < 5 and 0 <= nr < 5 and 0 <= nc < 5 and arr[nh][nr][nc] == 1 and visited[nh][nr][nc] == -1:
                visited[nh][nr][nc] = visited[h][r][c] + 1
                que.append([nh, nr, nc])
    res = visited[-1][-1][-1]
    return res if res != -1 else inf


def solve(plate_order, spin_order):
    answer = inf
    for p_order in plate_order:
        for s_order in spin_order:
            custom_maze = []
            for i in range(5):
                custom_maze.append(maze_type[p_order[i]][s_order[i]])
            travel = bfs(custom_maze)
            answer = min(answer, travel)
            if answer == 12:
                return answer
    return answer


inf = sys.maxsize
maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
maze_type = {x:[] for x in range(5)}

for height in range(5):
    plate = maze[height]
    for direction in range(4):
        new_plate = spin(height, plate)
        maze_type[height].append(new_plate)
        plate = new_plate

plate_order = []
permutation(5, 5, 0, [], [0 for _ in range(5)])

spin_order = []
product(4, 5, 0, [])

answer = solve(plate_order, spin_order)
print(answer if answer != inf else -1)
