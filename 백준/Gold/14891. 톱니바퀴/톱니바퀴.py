import sys
input = sys.stdin.readline


from collections import deque


N, M = 4, 8
gears = [list(map(int, list(input().rstrip()))) for _ in range(N)]
tops = [0]*N
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1
    visited = [0]*N
    visited[n] = d
    que = deque([[n, d]])
    while que:
        gear, direction = que.popleft()
        for new_gear in [gear-1, gear+1]:
            if 0 <= new_gear < N and visited[new_gear] == 0:
                if new_gear == gear-1:
                    left = gears[gear][(tops[gear]+6) % M]
                    new_right = gears[new_gear][(tops[new_gear]+2) % M]
                    if left != new_right:
                        visited[new_gear] = -1 * direction
                        que.append([new_gear, -1 * direction])
                elif new_gear == gear+1:
                    right = gears[gear][(tops[gear]+2) % M]
                    new_left = gears[new_gear][(tops[new_gear]+6) % M]
                    if right != new_left:
                        visited[new_gear] = -1 * direction
                        que.append([new_gear, -1 * direction])
    for i in range(N):
        if visited[i] == 1:
            tops[i] = (tops[i]+(M-1)) % M
        elif visited[i] == -1:
            tops[i] = (tops[i]+1) % M

ans = 0
for i in range(N):
    top = tops[i]
    if gears[i][top] == 1:
        ans += 2 ** i
print(ans)

