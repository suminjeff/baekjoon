import sys
input = sys.stdin.readline
from collections import deque

# 9205
t = int(input())
max_distance = 20*50
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    cvs = [list(map(int, input().split())) for _ in range(n)]
    ex, ey = map(int, input().split())
    visited = [0]*n
    que = deque([[sx, sy]])
    answer = "sad"
    while que:
        x, y = que.popleft()
        if abs(x-ex) + abs(y-ey) <= max_distance:
            answer = "happy"
            break
        for i in range(n):
            cx, cy = cvs[i]
            if visited[i] == 0 and abs(x-cx) + abs(y-cy) <= max_distance:
                visited[i] = 1
                que.append([cx, cy])
    print(answer)
