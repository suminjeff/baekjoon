import sys


graph = [
    # 시작점
    [1],  # 0

    # 둘레 칸
    [2], [3], [4], [5], [6, 21],  # 1~5
    [7], [8], [9], [10], [11, 24],  # 6~10
    [12], [13], [14], [15], [16, 26],  # 11~15
    [17], [18], [19], [20], [32],  # 16~20

    # 가로지르기 칸
    [22], [23], [29],  # 21~23
    [25], [29],  # 24~25
    [27], [28], [29],  # 26~28
    [30],  # 가운데 29
    [31], [20],  # 30~31

    # 도착점
    [32],  # 32
]

points = [
    # 시작점
    0,  # 0

    # 둘레 칸
    2, 4, 6, 8, 10,  # 1~5
    12, 14, 16, 18, 20,  # 6~10
    22, 24, 26, 28, 30,  # 11~15
    32, 34, 36, 38, 40,  # 16~20

    # 가로지르기 칸
    13, 16, 19,  # 21~23
    22, 24,  # 24~25
    28, 27, 26,  # 26~28
    25,  # 가운데 29
    30, 35,  # 30~31

    # 도착점
    0,  # 32
]

dice = list(map(int, input().split()))
piece = [0]*5
max_p = 0


def backtrack(depth, p):
    global max_p

    if depth == 10:
        max_p = max(max_p, p)
        return

    for i in range(1, 5):
        current_position = piece[i]

        if len(graph[current_position]) == 2:  # 파란 칸이면 파란 길로
            current_position = graph[current_position][1]
        else:
            current_position = graph[current_position][0]  # 빨간 칸이면 빨간 길로

        # 말 이동
        for _ in range(dice[depth]-1):
            current_position = graph[current_position][0]

        if current_position == 32 or (current_position < 32 and current_position not in piece):
            past_position = piece[i]
            piece[i] = current_position
            backtrack(depth + 1, p+points[current_position])
            piece[i] = past_position


backtrack(0, 0)
print(max_p)
