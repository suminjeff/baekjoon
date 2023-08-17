arr = [0]*1001

N = int(input())
last_idx = 0
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    if last_idx < L:
        last_idx = L

max_idx = arr.index(max(arr))

area = 0
left_H = 0
right_H = 0
for i in range(max_idx + 1):
    if left_H < arr[i]:
        left_H = arr[i]
    area += left_H

for i in range(last_idx, max_idx, -1):
    if right_H < arr[i]:
        right_H = arr[i]
    area += right_H

print(area)