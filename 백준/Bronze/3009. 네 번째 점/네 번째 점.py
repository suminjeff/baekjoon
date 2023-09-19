coor = [list(map(int, input().split())) for _ in range(3)]
for c in range(2):
    stack = []
    for r in range(3):
        v = coor[r][c]
        if stack:
            if v in stack:
                stack.remove(v)
            else:
                stack.append(v)
        else:
            stack.append(v)
    print(*stack, end=" ")