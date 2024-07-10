import sys
from collections import deque


# 20061


class Taxi:
    def __init__(self, position, fuel):
        self.position = position
        self.fuel = fuel

    def find_closest_passenger(self, n, grid, passenger_grid):
        r, c = self.position
        visited = [[-1]*n for _ in range(n)]
        visited[r][c] = 0
        que = deque([self.position])
        min_distance = sys.maxsize
        candidates = []
        while que:
            r, c = que.popleft()
            current_distance = visited[r][c]
            if current_distance > min_distance:
                break
            if passenger_grid[r][c] > 0:
                min_distance = min(min_distance, current_distance)
                candidates.append([r, c])
            else:
                for nr, nc in [[r-1, c], [r, c-1], [r, c+1], [r+1, c]]:
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and visited[nr][nc] == -1:
                        visited[nr][nc] = visited[r][c] + 1
                        que.append([nr, nc])

        if candidates:
            candidates.sort(key=lambda x:(x[0], x[1]))
            pr, pc = candidates[0]
            return True, passenger_grid[pr][pc], visited[pr][pc]
        return False, 0, -1

    def drive(self, n, destination, grid):
        r, c = self.position
        er, ec = destination
        visited = [[-1]*n for _ in range(n)]
        visited[r][c] = 0
        que = deque([self.position])
        while que:
            r, c = que.popleft()
            if r == er and c == ec:
                return visited[r][c]
            for nr, nc in [[r-1, c], [r, c-1], [r, c+1], [r+1, c]]:
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    que.append([nr, nc])
        return visited[er][ec]


class Passenger:
    def __init__(self, pk, position, destination):
        self.pk = pk
        self.position = position
        self.destination = destination


def get_passengers_data(n, m, passengers):
    '''
    손님 데이터 전처리
    passenger_grid: 손님 - 영역 지도 관계
    passenger_dict: 손님 pk - 손님 데이터 관계
    '''
    passenger_grid = [[0]*n for _ in range(n)]
    passenger_dict = {}
    pk = 1
    for i in range(m):
        sr, sc, er, ec = passengers[i]
        passenger = Passenger(pk, [sr, sc], [er, ec])
        passenger_dict[pk] = passenger
        passenger_grid[sr][sc] = pk
        pk += 1
    return passenger_grid, passenger_dict


def solve(n, m, fuel, grid, sr, sc, passengers):
    taxi = Taxi([sr, sc], fuel)
    passenger_grid, passenger_dict = get_passengers_data(n, m, passengers)
    
    # 손님이 남아 있을 때까지 반복
    while m:
        # 손님의 현위치
        # pk: 가장 가까운 손님 pk, fuel_required: 택시의 현위치에서 그 손님까지 가기 위한 연료량
        exists, pk, fuel_required = taxi.find_closest_passenger(n, grid, passenger_grid)

        # 손님이 남아 있는데 가장 가까운 손님을 찾을 수 없는 경우
        if not exists:
            return -1

        passenger = passenger_dict[pk]
        mr, mc = passenger.position

        # 만약 현재 위치에서 가장 가까운 손님까지 갈 수 없다면 -1 리턴
        if taxi.fuel < fuel_required:
            return -1

        # 만약 현재 위치에서 가장 가까운 손님까지 갈 수 있다면 데이터 업데이트
        passenger_grid[mr][mc] = 0
        taxi.fuel -= fuel_required
        taxi.position = [mr, mc]

        # 손님의 목적지
        destination = passenger.destination

        # drive_fuel: 택시의 현재 위치에서 목적지까지 가기 위한 연료량
        drive_fuel = taxi.drive(N, destination, grid)

        # 손님의 목적지까지 갈 수 없는 경우
        if drive_fuel == -1 or taxi.fuel < drive_fuel:
            return -1

        # 손님의 목적지까지 이동 가능하다면 연료 소모
        taxi.fuel -= drive_fuel

        # 목적지에서 소모한 연료의 두배 충전
        taxi.position = destination
        taxi.fuel += drive_fuel * 2

        m -= 1

    return taxi.fuel


if __name__ == '__main__':
    N, M, FUEL = map(int, input().split())
    GRID = [list(map(int, input().split())) for _ in range(N)]
    SR, SC = map(lambda x: int(x)-1, input().split())
    PASSENGERS = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    ANSWER = solve(N, M, FUEL, GRID, SR, SC, PASSENGERS)
    print(ANSWER)