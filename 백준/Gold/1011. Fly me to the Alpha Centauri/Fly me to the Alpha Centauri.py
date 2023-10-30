import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())
    d = y-x
    n = 0
    while True:
        if d <= n*(n+1):
            break
        n += 1
    if d <= n**2:
        print(n*2-1)
    else:
        print(n*2)