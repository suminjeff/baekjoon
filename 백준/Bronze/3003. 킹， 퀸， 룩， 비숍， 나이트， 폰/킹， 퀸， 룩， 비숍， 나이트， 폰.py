proper = [1, 1, 2, 2, 2, 8]
current = list(map(int, input().split()))

for i in range(len(proper)):
    print(proper[i] - current[i], end=" ")