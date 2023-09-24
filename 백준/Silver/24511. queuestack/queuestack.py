import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
v = 0
que = deque()
for i in range(N):
    if A[i] == 0:
        que.appendleft(B[i])
for c in C:
    que.append(c)
    print(que.popleft(), end=" ")