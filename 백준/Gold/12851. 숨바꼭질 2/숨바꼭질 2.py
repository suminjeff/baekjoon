import sys
input = sys.stdin.readline

from collections import deque


N, K = map(int, input().split())
arr = [0] * 100001
visited = [-1] * 100001
cnt = 0
visited[N] = 0
que = deque()
que.append([0, N])
min_depth = abs(N-K)
while que:
    depth, v = que.popleft()
    if depth > min_depth:
        continue
    if v == K:
        if min_depth >= depth:
            visited[v] = depth
            cnt += 1
    for nv in [v+1, v-1, 2*v]:
        if 0 <= nv < 100001:
            if visited[nv] == -1 or visited[nv] >= depth+1:
                visited[nv] = depth+1
                que.append([depth+1, nv])
print(visited[K])
print(cnt)