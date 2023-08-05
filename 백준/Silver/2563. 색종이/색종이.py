N = int(input())
square_size = 10
canvas_size = 100
canvas = [[False] * canvas_size for _ in range(canvas_size)]

for b in range(N):
    x, y = map(int, input().split())
    for row in range(x, x+10):
        for col in range(y, y+10):
            canvas[row][col] = True

count = 0
for row in range(canvas_size):
    for col in range(canvas_size):
        if canvas[row][col]:
            count += 1

print(count)
