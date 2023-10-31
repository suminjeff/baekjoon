import sys
input = sys.stdin.readline

from collections import deque


def move(x, y, dx, dy):
    cnt = 1
    while arr[x+dx][y+dy] != "#" and arr[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs(rx, ry, bx, by):
    que = deque([(rx, ry, bx, by, 1)])
    while que:
        rx, ry, bx, by, depth = que.popleft()
        if depth > 10:
            break
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nrx, nry, rcnt = move(rx, ry, dx, dy)
            nbx, nby, bcnt = move(bx, by, dx, dy)
            if arr[nbx][nby] == "O":
                continue
            if arr[nrx][nry] == "O":
                print(depth)
                return
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                que.append((nrx, nry, nbx, nby, depth+1))
    print(-1)


# 각각의 동작에서 공은 동시에 움직인다
# 빨간 구슬이 구멍에 빠지면 성공이지만 파란 구슬이 구멍에 빠지면 실패다
# 빨간 구슬과 파란 구슬이 동싱에 구멍에 빠져도 실패다
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다
# 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다

# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하기

N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

rx, ry, bx, by = [0]*4
for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            rx, ry = i, j
        elif arr[i][j] == "B":
            bx, by = i, j
visited[rx][ry][bx][by] = 1
bfs(rx, ry, bx, by)