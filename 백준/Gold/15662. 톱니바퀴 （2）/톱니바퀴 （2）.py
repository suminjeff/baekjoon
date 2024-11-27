import sys

from collections import deque


def solve(t: int, status: list[deque[str]], k: int, rotate: list[list[int]]) -> int:
    right_index, left_index = 2, 6

    for i in range(k):
        index, direction = rotate[i]
        index -= 1

        turn = [0] * t
        turn[index] = direction

        temp_t = index  # 비교 기준 톱니바퀴
        # 회전시킬 톱니바퀴의 오른쪽에 있는 톱니바퀴들 확인
        for j in range(index+1, t):
            if status[temp_t][right_index] != status[j][left_index]:
                turn[j] = -turn[temp_t]
            else:
                break
            temp_t = j
        temp_t = index
        # 회전시킬 톱니바퀴의 왼쪽에 있는 톱니바퀴들 확인
        for j in range(index-1, -1, -1):
            if status[temp_t][left_index] != status[j][right_index]:
                turn[j] = -turn[temp_t]
            else:
                break
            temp_t = j

        # 정해진 회전 방향에 따라 돌리기
        for j in range(t):
            status[j].rotate(turn[j])

    answer = sum(list(map(lambda x: 1 if x[0] == '1' else 0, status)))

    return answer


if __name__ == "__main__":
    T = int(input())
    STATUS = [deque(list(input())) for _ in range(T)]
    K = int(input())
    ROTATE = [list(map(int, input().split())) for _ in range(K)]
    ANSWER = solve(T, STATUS, K, ROTATE)
    print(ANSWER)