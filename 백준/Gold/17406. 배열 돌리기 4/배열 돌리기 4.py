import sys
input = sys.stdin.readline

from collections import deque
from copy import deepcopy




def min_row(arr):
    res = 50 * 100
    for row in range(N):
        res = min(res, sum(arr[row]))
    return res


def turn(row, col, s):
    que = deque()
    for i in range(1, s + 1):
        rt, rb = row - i, row + i
        cl, cr = col - i, col + i
        r, c = rt, cl
        limit = 8 * i
        while limit > 0:
            while c < cr:
                que.append(arr[r][c])
                c += 1
                limit -= 1
            while r < rb:
                que.append(arr[r][c])
                r += 1
                limit -= 1
            while c > cl:
                que.append(arr[r][c])
                c -= 1
                limit -= 1
            while r > rt:
                que.append(arr[r][c])
                r -= 1
                limit -= 1
        nr, nc = rt, cl + 1
        while que:
            while nc < cr:
                arr[nr][nc] = que.popleft()
                nc += 1
            while nr < rb:
                arr[nr][nc] = que.popleft()
                nr += 1
            while nc > cl:
                arr[nr][nc] = que.popleft()
                nc -= 1
            while nr >= rt:
                arr[nr][nc] = que.popleft()
                nr -= 1

def perm(array, n):
    if len(array) == n:
        permutations.append(array[:])
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            array.append(i)
            perm(array, n)
            array.pop()
            visited[i] = 0


N, M, K = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]
arr = deepcopy(input_arr)
turn_info = [list(map(int, input().split())) for _ in range(K)]
permutations = []
visited = [0] * K
perm([], K)
ans = 50 * 100
for perm in permutations:
    for i in range(K):
        order = perm[i]
        r, c, s = turn_info[order]
        turn(r-1, c-1, s)
    ans = min(ans, min_row(arr))
    arr = deepcopy(input_arr)
print(ans)
