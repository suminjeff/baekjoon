import sys
input = sys.stdin.readline


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    cache = {*points}
    ans = 0
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]
            dx, dy = x1-x2, y1-y2
            if ((x1-dy, y1+dx) in cache and (x2-dy, y2+dx) in cache) or ((x1-dy, y1+dx) in cache and (x2-dy, y2+dx) in cache):
                ans = max(ans, dx**2+dy**2)
    print(ans)
