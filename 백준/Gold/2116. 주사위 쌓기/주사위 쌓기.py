def my_max(iterable):
    max_v = iterable[0]
    for v in iterable:
        if max_v < v:
            max_v = v
    return max_v


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
max_side = 0
for i in range(6):
    col = i
    side = 0
    row = 0

    while row < N:
        temp = [n for n in range(1, 7)]
        bottom = arr[row][col]
        top = arr[row][pair[col]]
        temp.remove(bottom)
        temp.remove(top)
        side += my_max(temp)

        if row < N-1:
            for c in range(6):
                if arr[row+1][c] == top:
                    col = c
                    break
        row += 1

    if max_side < side:
        max_side = side

print(max_side)
