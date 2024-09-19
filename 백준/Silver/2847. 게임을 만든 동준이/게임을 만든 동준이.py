import sys


def solve(n, points):
    before_point = points[n-1]
    answer = 0
    for level in range(n-2, -1, -1):
        current_point = points[level]
        while before_point <= current_point:
            current_point -= 1
            answer += 1
        before_point = current_point
    return answer


if __name__ == '__main__':
    N = int(input())
    POINTS = [int(input()) for _ in range(N)]
    ANSWER = solve(N, POINTS)
    print(ANSWER)