import sys
input = sys.stdin.readline


from collections import deque

N = int(input())
que = deque([i for i in range(N, 0, -1)])
while len(que) > 1:
    que.pop()
    que.appendleft(que.pop())
print(que[0])