import sys
input = sys.stdin.readline


def func(command, num=0):
    global top
    if command == 1:
        top += 1
        stack[top] = num
    elif command == 2:
        if top > -1:
            top -= 1
            print(stack[top+1])
        else:
            print(top)
    elif command == 3:
        print(top + 1)
    elif command == 4:
        print(int(top == -1))
    elif command == 5:
        p = top if top == -1 else stack[top]
        print(p)


N = int(input())
stack = [0] * N
top = -1
for _ in range(N):
    inp = list(map(int, input().split()))
    cmd = inp[0]
    if inp[0] == 1:
        n = inp[1]
        func(cmd, n)
    else:
        func(cmd)