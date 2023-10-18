import sys
input = sys.stdin.readline

from collections import deque


def bfs(start, depth):
    que = deque()
    que.append([start, depth])
    while que:
        n, depth = que.popleft()
        if n == B:
            return depth
        if int(n)*2 <= int(B):
            que.append([str(int(n)*2), depth+1])
        if int(n+"1") <= int(B):
            que.append([str(int(n+"1")), depth+1])
    return -1


A, B = input().split()
print(bfs(A, 1))
