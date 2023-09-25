import sys
input = sys.stdin.readline

from collections import deque


def cmd(command):
    c = command[0]
    if c == "push_front":
        v = command[1]
        que.appendleft(v)
    elif c == "push_back":
        v = command[1]
        que.append(v)
    elif c == "pop_front":
        print(que.popleft() if que else -1)
    elif c == "pop_back":
        print(que.pop() if que else -1)
    elif c == "size":
        print(len(que))
    elif c == "empty":
        print(int(len(que) == 0))
    elif c == "front":
        print(que[0] if que else -1)
    elif c == "back":
        print(que[-1] if que else -1)


N = int(input())
que = deque()
for _ in range(N):
    command = list(input().split())
    cmd(command)
