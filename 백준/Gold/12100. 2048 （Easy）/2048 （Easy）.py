import copy
from itertools import product


def swipe(number):
    global N

    # up
    if number == 1:
        for col in range(N):
            stack = []
            doubled = []
            top = -1
            for row in range(N):
                v = arr[row][col]
                if v != 0:
                    if stack:
                        if v == stack[top]:
                            stack[top] = str(stack[top] + v)
                            arr[row][col] = 0
                            continue
                    stack.append(v)
                    top += 1
                    arr[row][col] = 0
            row = 0
            while stack:
                v = stack.pop(0)
                arr[row][col] = int(v)
                row += 1

    # down
    elif number == 2:
        for col in range(N):
            stack = []
            top = -1
            for row in range(N-1, -1, -1):
                v = arr[row][col]
                if v != 0:
                    if stack:
                        if v == stack[top]:
                            stack[top] = str(stack[top] + v)
                            arr[row][col] = 0
                            continue
                    stack.append(v)
                    top += 1
                    arr[row][col] = 0
            row = N-1
            while stack:
                v = stack.pop(0)
                arr[row][col] = int(v)
                row -= 1
    # left
    elif number == 3:
        for row in range(N):
            stack = []
            top = -1
            for col in range(N):
                v = arr[row][col]
                if v != 0:
                    if stack:
                        if v == stack[top]:
                            stack[top] = str(stack[top] + v)
                            arr[row][col] = 0
                            continue
                    stack.append(v)
                    top += 1
                    arr[row][col] = 0
            col = 0
            while stack:
                v = stack.pop(0)
                arr[row][col] = int(v)
                col += 1
    # right
    elif number == 4:
        for row in range(N):
            stack = []
            top = -1
            for col in range(N-1, -1, -1):
                v = arr[row][col]
                if v != 0:
                    if stack:
                        if v == stack[top]:
                            stack[top] = str(stack[top] + v)
                            arr[row][col] = 0
                            continue
                    stack.append(v)
                    top += 1
                    arr[row][col] = 0
            col = N-1
            while stack:
                v = stack.pop(0)
                arr[row][col] = int(v)
                col -= 1


N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]
# 1 = up, 2 = down, 3 = left, 4 = right
moves = [1, 2, 3, 4]
ans = 0

for move in product(moves, repeat=5):
    arr = copy.deepcopy(input_arr)
    for i in move:
        swipe(i)
    max_v = 0
    for r in range(N):
        for c in range(N):
            if max_v < arr[r][c]:
                max_v = arr[r][c]
    ans = max(ans, max_v)
print(ans)
