import sys
from collections import deque


def solve(n, m, switch_data):
    # 스위치 좌표와 불 좌표 그래프
    graph = [[[] for _ in range(N)] for _ in range(N)]
    graph[0][0].append([0, 0])

    for x, y, a, b in switch_data:
        graph[x-1][y-1].append([a-1, b-1])

    light = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque([[0, 0]])

    while que:
        x, y = que.popleft()
        for sx, sy in graph[x][y]:
            if light[sx][sy] == 0:
                light[sx][sy] = 1
                if visited[sx][sy] == 1:
                    que.append([sx, sy])

        for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if light[nx][ny] == 1:
                    que.append([nx, ny])

    result = sum([sum(row) for row in light])

    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    SWITCH_DATA = [list(map(int, input().split())) for _ in range(M)]
    answer = solve(N, M, SWITCH_DATA)
    print(answer)