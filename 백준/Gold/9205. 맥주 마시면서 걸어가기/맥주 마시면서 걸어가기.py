import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    que = deque()
    home = list(map(int, input().split()))
    cvs = []
    visited = [0]*N
    for i in range(N):
        x, y = map(int, input().split())
        cvs.append([x, y])
    gx, gy = list(map(int, input().split()))

    que = deque()
    que.append(home)
    ans = "sad"
    while que:
        r, c = que.popleft()
        if abs(r-gx) + abs(c-gy) <= 1000:
            ans = "happy"
            break
        for i in range(N):
            if not visited[i]:
                nr, nc = cvs[i]
                if abs(r-nr) + abs(c-nc) <= 1000:
                    visited[i] = 1
                    que.append([nr, nc])
    print(ans)