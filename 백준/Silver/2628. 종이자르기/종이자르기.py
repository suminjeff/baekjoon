M, N = map(int, input().split())
T = int(input())


base = [0, M]
height = [0, N]
for _ in range(T):
    way, idx = map(int, input().split())
    if way == 0: # 가로
        height.append(idx)
    elif way == 1: # 세로
        base.append(idx)
base.sort()
height.sort()

max_base = 0
for i in range(len(base)-1):
    if max_base < abs(base[i] - base[i+1]):
        max_base = abs(base[i] - base[i+1])

max_height = 0
for i in range(len(height)-1):
    if max_height < abs(height[i] - height[i+1]):
        max_height = abs(height[i] - height[i+1])
print(max_base * max_height)