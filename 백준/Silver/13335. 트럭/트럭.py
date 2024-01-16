import sys
input = sys.stdin.readline


# 13335

from collections import deque
N, W, L = map(int, input().split())
K = N
truck = list(map(int, input().split()))
bridge = deque([0]*W)
weight, order, time = 0, 0, 0
while K:
    # 만약 현재 하중 + 들어올 트럭의 하중이 최대 하중보다 같거나 작다면
    # 현재 하중에 들어올 트럭의 하중을 더해주고
    # 다리 큐를 한칸씩 앞으로 움직이기
    crossed = bridge.popleft()
    if crossed > 0:
        K -= 1
        weight -= crossed
    if order < N:
        if weight+truck[order] <= L:
            weight += truck[order]
            bridge.append(truck[order])
            order += 1
        else:
            bridge.append(0)
    else:
        bridge.append(0)
    time += 1
print(time)