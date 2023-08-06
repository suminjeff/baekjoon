arr = [input() for _ in range(5)]

max_len = 0
for word in arr:
    if max_len < len(word):
        max_len = len(word)

for col in range(max_len):
    for row in range(5):
        if col < len(arr[row]):
            print(arr[row][col], end='')