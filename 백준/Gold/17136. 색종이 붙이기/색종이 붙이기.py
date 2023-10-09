import sys
input = sys.stdin.readline


def check_size(i, j):
    for s in range(5, 0, -1):
        flag = True
        for r in range(i, i+s):
            for c in range(j, j+s):
                if r >= N or c >= N or arr[r][c] == 0:
                    flag = False
                    break
        if flag:
            return s


def cover(i, j, s):
    for r in range(i, i+s):
        for c in range(j, j+s):
            arr[r][c] = 0


def uncover(i, j, s):
    for r in range(i, i+s):
        for c in range(j, j+s):
            arr[r][c] = 1


def dfs(cnt):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                max_size = check_size(i, j)
                for s in range(max_size, 0, -1):
                    if paper[s]:
                        cover(i, j, s)
                        paper[s] -= 1
                        res.add(dfs(cnt+1))
                        uncover(i, j, s)
                        paper[s] += 1
                if res:
                    return min(res)
                else:
                    return -1
    return cnt

paper = [0, 5, 5, 5, 5, 5]

N = 10
arr = [list(map(int, input().split())) for _ in range(N)]
res = set()
min_cnt = float('inf')
res.add(dfs(0))
if -1 in res:
    res.remove(-1)
print(min(res) if res else -1)