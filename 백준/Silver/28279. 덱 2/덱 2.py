import sys
input = sys.stdin.readline

from collections import deque


def cmd(command):
    c = command[0]
    if c == 1:
        v = command[1]
        que.appendleft(v)
    elif c == 2:
        v = command[1]
        que.append(v)
    elif c == 3:
        print(que.popleft() if que else -1)
    elif c == 4:
        print(que.pop() if que else -1)
    elif c == 5:
        print(len(que))
    elif c == 6:
        print(int(len(que) == 0))
    elif c == 7:
        print(que[0] if que else -1)
    elif c == 8:
        print(que[-1] if que else -1)


N = int(input())
que = deque()
for _ in range(N):
    command = list(map(int, input().split()))
    cmd(command)
