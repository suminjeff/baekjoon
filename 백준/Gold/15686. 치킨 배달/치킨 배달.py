import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
C = 0
# 1. 치킨집 위치와 개수 구하기, 집 위치 구하기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])
            C += 1

# 2. 치킨집들 중 최대 M개의 폐업시키지 않을 치킨집을 고르기 (부분집합 생성)
subset_list = []
for i in range(1 << C):
    temp = []
    for j in range(C):
        if i & (1 << j):
            temp.append(chicken[j])
    if 0 < len(temp) <= M:
        subset_list.append(temp)

# 3. 부분집합마다 돌면서 최소거리 갱신
res = float("inf")
for subset in subset_list:
    dist = 0
    for h_loc in house:
        i, j = h_loc
        min_dist = 2*N
        for c_loc in subset:
            r, c = c_loc
            min_dist = min(min_dist, abs(i-r) + abs(j-c))
        dist += min_dist
    res = min(res, dist)
print(res)