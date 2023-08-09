def get_max():
    global max_len
    for i in range(N):
        length = 1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                length += 1
                if max_len < length:
                    max_len = length
            else:
                length = 1
    for j in range(N):
        length = 1
        for i in range(N-1):
            if arr[i][j] == arr[i+1][j]:
                length += 1
                if max_len < length:
                    max_len = length
            else:
                length = 1


N = int(input())
arr = [list(input()) for _ in range(N)]
max_len = 1

for row in range(N):
    for col in range(N-1):
        arr[row][col], arr[row][col+1] = arr[row][col+1], arr[row][col]
        get_max()
        arr[row][col + 1], arr[row][col] = arr[row][col], arr[row][col + 1]
for col in range(N):
    for row in range(N-1):
        arr[row][col], arr[row+1][col] = arr[row+1][col], arr[row][col]
        get_max()
        arr[row+1][col], arr[row][col] = arr[row][col], arr[row+1][col]

get_max()
print(max_len)
