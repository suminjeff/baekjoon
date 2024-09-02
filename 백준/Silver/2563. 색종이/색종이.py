import sys


def solve(n, position):
    answer = 0
    canvas = [[0]*max(map(lambda x:x[0]+10+1, position)) for _ in range(max(map(lambda x:x[1]+10+1, position)))]
    for x, y in position:
        for r in range(y, y+10):
            for c in range(x, x+10):
                if canvas[r][c] == 0:
                    canvas[r][c] = 1
                    answer += 1
    return answer


if __name__ == '__main__':
    N = int(input())
    POSITION = [list(map(int, input().split())) for _ in range(N)]
    ANSWER = solve(N, POSITION)
    print(ANSWER)
