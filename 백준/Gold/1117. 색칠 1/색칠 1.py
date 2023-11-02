import sys
input = sys.stdin.readline
W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

area = (c+1)*(x2-x1)*(y2-y1)
if f <= W//2:
    if f <= x1:
        print(W*H - area)
    else:
        print(W*H - (area+(min(f, x2)-x1) * (y2-y1) * (c+1)))
else:
    if W <= x1+f:
        print(W*H - area)
    else:
        print(W*H - (area + (min(W, f+x2) - (f+x1)) * (y2-y1)*(c+1)))
