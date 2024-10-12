import sys
from collections import deque


def solve(n, m, r, c, d, room):

    answer = 0
    cleaned = [[0]*m for _ in range(n)]
    que = deque([(r, c, d)])  # 시작점

    while que:
        x, y, direction = que.popleft()
        # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if cleaned[x][y] == 0:
            cleaned[x][y] = 1
            answer += 1

        flag = False
        for dx, dy in zip(DX, DY):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0 and cleaned[nx][ny] == 0:
                flag = True

        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        if not flag:
            # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            dx, dy = DX[direction], DY[direction]
            onx, ony = x - dx, y - dy
            if 0 <= onx < n and 0 <= ony < m and room[onx][ony] == 0:
                que.append((onx, ony, direction))
            # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        else:
            for _ in range(4):
                # 3-1. 반시계 방향으로 90도 회전한다.
                direction = (direction - 1) if direction >= 1 else 3
                # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                dx, dy = DX[direction], DY[direction]
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0 and cleaned[nx][ny] == 0:
                    que.append((nx, ny, direction))
                    break
    return answer


if __name__ == '__main__':
    # const
    DX, DY = [-1, 0, 1, 0], [0, 1, 0, -1]

    # input
    N, M = map(int, input().split())
    R, C, D = map(int, input().split())
    ROOM = [list(map(int, input().split())) for _ in range(N)]

    # answer
    ANSWER = solve(N, M, R, C, D, ROOM)
    print(ANSWER)