import sys
import copy

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

area = 0
cctv_list = []
for i in range(N):
    for j in range(M):
        v = arr[i][j]
        if v == 0:
            area += 1
        if 0 < v < 6:
            cctv_list.append([v, i, j])

def watch(arr, direction, r, c):
    for d in direction:
        nr, nc = r, c
        while True:
            nr += dr[d]
            nc += dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6:
                    break
                if arr[nr][nc] == 0:
                    arr[nr][nc] = -1
            else:
                break


def backtrack(depth, arr):
    global ans
    if depth == len(cctv_list):
        cnt = 0
        for i in range(N):
            cnt += arr[i].count(0)
        ans = min(ans, cnt)
        return

    temp = copy.deepcopy(arr)
    cctv_type, r, c = cctv_list[depth]
    for d in direction[cctv_type]:
        watch(temp, d, r, c)
        backtrack(depth+1, temp)
        temp = copy.deepcopy(arr)


ans = sys.maxsize
backtrack(0, arr)
print(ans)