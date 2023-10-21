# 9: 아기상어의 위치
# 1~6: 물고기의 크기
# 이동 조건
# 1. 자신보다 크기가 큰 물고기가 있는 칸은 지날 수 없고 나머지 (같거나 작은) 칸은 모두 지날 수 있음
# 2. 자신보다 크기가 작은 물고기만 먹을 수 있음
# 이동 방법
#     a) 더 이상 먹을 수 있는 물고기가 없다면 어미 상어에게 도움을 청한다.
#     b) 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다.
#     c) 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운(지나야하는 칸의 개수의 최솟값) 물고기를 먹으러 간다.
#         i. 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 떄, 지나야하는 칸의 개수의 최솟값
#        ii. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다
# 2. 이동은 1초 걸리고, 물고기를 먹는 데에 걸리는 시간은 없다고 가정 (즉, 이동 즉시 먹음)
#     - 물고기를 먹으면 그 칸은 빈 칸이 됨
# 3. 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
# 문제 : 아기 상어가 몇 초 동안 엄마 상어에게 도움을 청하지 않고 물고기를 잡아먹을 수 있는지 구하기

import sys
input = sys.stdin.readline

from collections import deque
import heapq

def starting_point():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return [i, j]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = starting_point()
size = 2
eat = 0
arr[start[0]][start[1]] = 0
ans = 0
while True:
    que = deque()
    que.append([start, 0])
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    min_depth = float('inf')
    # 먹을 수 있는 물고기 후보 찾기
    candidates = []
    while que:
        coordinate, depth = que.popleft()
        if depth <= min_depth:
            r, c = coordinate
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if 0 <= nr < N and 0 <= nc < N and 0 <= arr[nr][nc] <= size and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    if 0 < arr[nr][nc] < size:
                        min_depth = min(min_depth, depth+1)
                        heapq.heappush(candidates, [depth+1, nr, nc])
                    else:
                        que.append([[nr, nc], depth+1])
    # break
    if candidates:
        distance, fr, fc = heapq.heappop(candidates)
        arr[fr][fc] = 0
        start = [fr, fc]
        eat += 1
        ans += distance
        if eat == size:
            eat = 0
            size += 1
    else:
        break
print(ans)