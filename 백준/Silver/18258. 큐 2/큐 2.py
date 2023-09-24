import sys
input = sys.stdin.readline


def q(command):
    global front
    global rear
    c = command[0]
    if c == "push":
        rear += 1
        que[rear] = command[1]
    elif c == "pop":
        if front == rear:
            print(-1)
        else:
            front += 1
            print(que[front])
    elif c == "size":
        print(rear - front)
    elif c == "empty":
        print(int(front == rear))
    elif c == "front":
        print(que[front+1] if front != rear else -1)
    elif c == "back":
        print(que[rear] if front != rear else -1)


N = int(input())
que = [0] * N
front = rear = -1
for _ in range(N):
    v = list(map(str, input().split()))
    q(v)
