import sys
input = sys.stdin.readline

from math import gcd


N = int(input())
diff = []
first = int(input())
for _ in range(1, N):
    pos = int(input())
    diff.append(abs(first - pos))
    first = pos
g = diff[0]
for i in range(1, len(diff)):
    g = gcd(g, diff[i])

cnt = 0
for d in diff:
    cnt += d // g - 1
print(cnt)