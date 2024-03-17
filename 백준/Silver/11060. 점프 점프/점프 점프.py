import sys
from collections import deque

# 11060

N = int(input())
A = list(map(int, input().split()))
V = [0]+[-1]*(N-1)
que = deque([[A[0], 0]])
while que:
    k, v = que.popleft()
    for jump in range(1, k+1):
        nv = v + jump
        if nv < N and V[nv] == -1:
            V[nv] = V[v] + 1
            que.append([A[nv], nv])
print(V[-1])