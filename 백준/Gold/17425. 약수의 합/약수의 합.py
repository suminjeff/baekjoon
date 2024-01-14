import sys
input = sys.stdin.readline

T = int(input())
MAX = 1000000
f = [0] + [1]*MAX
g = [0]*(MAX+1)
for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        f[i*j] += i
        j += 1
for i in range(1, MAX+1):
    g[i] = g[i-1] + f[i]
for _ in range(T):
    N = int(input())
    print(g[N])
