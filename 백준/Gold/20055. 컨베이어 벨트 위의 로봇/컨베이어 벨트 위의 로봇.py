import sys
from collections import deque
input = sys.stdin.readline


# 20055 컨베이어 벨트 위의 로봇

N, K = map(int, input().split())
arr = deque(list(map(int, input().split())))
robot = deque([0]*N)
stage = 0
while True:
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(N-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and arr[i+1] > 0:
                robot[i], robot[i+1] = 0, 1
                arr[i+1] -= 1
        robot[-1] = 0
    if robot[0] == 0 and arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1
    stage += 1
    if arr.count(0) >= K:
        break
print(stage)