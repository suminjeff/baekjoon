import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    visited = [0]*10001
    que = deque()
    que.append([A, ''])
    visited[A] = 1
    while que:
        n, history = que.popleft()

        if n == B:
            print(history)
            break

        # D
        d = n * 2 % 10000
        if visited[d] == 0:
            visited[d] = 1
            que.append([d, history+'D'])

        # S
        s = (n - 1) % 10000
        if visited[s] == 0:
            visited[s] = 1
            que.append([s, history+'S'])

        # L
        l = n // 1000 + (n % 1000) * 10
        if visited[l] == 0:
            visited[l] = 1
            que.append([l, history+'L'])

        # R
        r = n // 10 + (n % 10) * 1000
        if visited[r] == 0:
            visited[r] = 1
            que.append([r, history+'R'])
