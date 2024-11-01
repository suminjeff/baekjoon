import sys

N = int(input())
candies = [list(input()) for _ in range(N)]



def get_max_v():
    max_v = 0
    # 행 방향
    for i in range(N):
        color = candies[i][0]
        v = 1
        for j in range(1, N):
            if candies[i][j] == color:
                v += 1
            else:
                color = candies[i][j]
                max_v = max(max_v, v)
                v = 1
        max_v = max(max_v, v)
    # 열 방향
    for j in range(N):
        color = candies[0][j]
        v = 1
        for i in range(1, N):
            if candies[i][j] == color:
                v += 1
            else:
                color = candies[i][j]
                max_v = max(max_v, v)
                v = 1
        max_v = max(max_v, v)
    return max_v


# 1단계: 초기에 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분의 길이를 찾는다.
max_v = get_max_v()

# 2단계: (0, 0)부터 돌면서 서로 다른 색깔인 인접한 두 칸의 색깔을 바꾸고 max_v를 확인한다.
# 행 방향
for i in range(N):
    for j in range(1, N):
        a, b = candies[i][j-1], candies[i][j]
        if a != b:
            candies[i][j-1], candies[i][j] = candies[i][j], candies[i][j-1]  # 위치 바꾸기
            tmp_max_v = get_max_v()  # 바뀐 상태에서 max_v 계산
            max_v = max(max_v, tmp_max_v)  # max_v 갱신
            candies[i][j-1], candies[i][j] = candies[i][j], candies[i][j-1]  # 위치 되돌려놓기

# 열 방향
for j in range(N):
    for i in range(1, N):
        a, b = candies[i-1][j], candies[i][j]
        if a != b:
            candies[i-1][j], candies[i][j] = candies[i][j], candies[i-1][j]  # 위치 바꾸기
            tmp_max_v = get_max_v()  # 바뀐 상태에서 max_v 계산
            max_v = max(max_v, tmp_max_v)  # max_v 갱신
            candies[i-1][j], candies[i][j] = candies[i][j], candies[i-1][j]  # 위치 되돌려놓기

print(max_v)
