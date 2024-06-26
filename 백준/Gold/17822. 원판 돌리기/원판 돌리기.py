import sys
from collections import deque


def solve(n, m, t, plates, rotations):
    total_score, total_count = 0, n*m
    for plate in plates:
        total_score += sum(plate)
    for x, d, k in rotations:
        # 1. 번호가 x의 배수인 원판을 d 방향으로 k칸 회전
        for i in range(1, n+1):
            if i % x == 0:
                for _ in range(k % m):
                    # d가 0: 시계 방향, 1: 반시계 방향
                    # 1123 -> 3112
                    if d == 0:
                        plates[i].rotate(1)
                    # 1123 -> 1231
                    elif d == 1:
                        plates[i].rotate(-1)
        # 2. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾음
        if total_score > 0:
            same_numbers_index, visited = set(), [[0]*m for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(m):
                    if plates[i][j] > 0 and visited[i][j] == 0:
                        add_first_index = False
                        number = plates[i][j]
                        visited[i][j] = 1
                        que = deque([[i, j]])
                        while que:
                            r, c = que.popleft()
                            for nr, nc in [[r+1, c], [r-1, c], [r, (c+1)%m], [r, (c-1)%m]]:
                                if 1 <= nr < n+1 and 0 <= nc < m and visited[nr][nc] == 0 and plates[nr][nc] == number:
                                    add_first_index = True
                                    same_numbers_index.add((nr, nc))
                                    visited[nr][nc] = 1
                                    que.append([nr, nc])
                        if add_first_index:
                            same_numbers_index.add((i, j))
            # 3-1. 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지움
            if same_numbers_index:
                for i, j in same_numbers_index:
                    total_score -= plates[i][j]
                    total_count -= 1
                    plates[i][j] = 0
            # 3-2. 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더함
            else:
                average = total_score / total_count
                for i in range(1, n+1):
                    for j in range(m):
                        v = plates[i][j]
                        if v > 0:
                            if v > average:
                                plates[i][j] -= 1
                                total_score -= 1
                            elif v < average:
                                plates[i][j] += 1
                                total_score += 1
    return total_score


if __name__ == '__main__':
    N, M, T = map(int, input().split())
    PLATES = [[]] + [deque(list(map(int, input().split()))) for _ in range(N)]
    ROTATIONS = [list(map(int, input().split())) for _ in range(T)]
    answer = solve(N, M, T, PLATES, ROTATIONS)
    print(answer)
