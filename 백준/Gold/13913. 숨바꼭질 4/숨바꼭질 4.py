import sys
input = sys.stdin.readline
from collections import deque


MAX = 10**5+1
N, K = map(int, input().split())
visited = [0]*MAX
visited[N] = 0
path = f"{N}"
que = deque([[N, path]])
while que:
    v, p = que.popleft()
    if v == K:
        print(visited[K])
        print(*p.split("-"))
        break
    for nv in [2*v, v+1, v-1]:
        if v == 0 and nv == 2*v:
            continue
        if 0 <= nv < MAX and visited[nv] == 0:
            visited[nv] = visited[v]+1
            que.append([nv, p+f"-{nv}"])
