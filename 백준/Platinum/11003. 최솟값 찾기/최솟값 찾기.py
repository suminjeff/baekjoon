import sys
input = sys.stdin.readline
from collections import deque

# 11003

N, L = map(int, input().split())
A = list(map(int, input().split()))

window = deque()

ans = []
length = 0
for i in range(N):
    v = A[i]
    while window and window[-1][0] >= v:
        window.pop()
    window.append([v, i])
    while window[0][1] < i-L+1:
        window.popleft()
    ans.append(window[0][0])

print(*ans)