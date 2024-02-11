import sys
input = sys.stdin.readline
# 1158

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
i = K-1
res = []
while arr:
    res.append(arr.pop(i))
    N -= 1
    if i >= N:
        i = 0
    if N == 0:
        break
    i = (i + K-1) % N
print("<", end="")
print(*res, sep=', ', end="")
print(">", end="")