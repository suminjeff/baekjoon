import sys


def fail(x: int):
    return f'kraj {x}'


def get_distance(x1: int, y1: int, x2: int, y2: int):
    return abs(x1-x2) + abs(y1-y2)


# (cr, cc): 미친 아두이노의 위치, (tr, tc): 종수의 위치
def get_next_position(cr: int, cc: int, tr: int, tc: int):
    min_distance = sys.maxsize
    next_position = []
    for d, delta in DELTA.items():
        dr, dc = delta
        nr, nc = cr+dr, cc+dc
        distance = get_distance(nr, nc, tr, tc)
        if min_distance > distance:
            min_distance = distance
            next_position = [nr, nc]
    return next_position


def solve(r: int, c: int, board: list[list[str]], direction: list):

    jong_su = dict()
    crazy_arduino = dict()
    ca_pk = 1
    # 종수와 미친 아두이노들의 위치 찾기
    for i in range(r):
        for j in range(c):
            if board[i][j] == JONG_SU:
                jong_su.setdefault('status', {
                    'current_position': [i, j],
                    'next_position': []
                })
            elif board[i][j] == CRAZY_ARDUINO:
                crazy_arduino.setdefault(ca_pk, {
                    'current_position': [i, j],
                    'next_position': [],
                })
                ca_pk += 1

    x = 0
    # 주어진 방향대로 종수를 움직이기
    for d in direction:

        next_position = {}
        # 종수의 이동
        jr, jc = jong_su['status']['current_position']
        dr, dc = DELTA[d]
        nr, nc = jr+dr, jc+dc
        jong_su['status']['next_position'] = [nr, nc]
        x += 1

        # 미친 아두이노들의 다음 이동 위치 확인
        for pk, status in crazy_arduino.items():
            cr, cc = status.get('current_position')
            ncr, ncc = get_next_position(cr, cc, nr, nc)
            if (ncr, ncc) not in next_position:
                next_position.setdefault((ncr, ncc), [])
            next_position[(ncr, ncc)].append([pk, cr, cc])

        # 미친 아두이노들의 다음 이동 위치에 무엇이 있는지 확인
        for next_coordinate, current_coordinates in next_position.items():
            ncr, ncc = next_coordinate
            if ncr == nr and ncc == nc:
                return fail(x)
            if len(current_coordinates) == 1:
                pk, cr, cc = current_coordinates[0]
                crazy_arduino[pk]['next_position'] = [ncr, ncc]
            elif len(current_coordinates) > 1:
                for pk, cr, cc in current_coordinates:
                    crazy_arduino.pop(pk)
                    board[cr][cc] = SPACE
        # 실제 보드에 반영
        jong_su['status']['current_position'] = [nr, nc]
        board[jr][jc], board[nr][nc] = board[nr][nc], board[jr][jc]
        for pk, status in crazy_arduino.items():
            cr, cc = status['current_position']
            crazy_arduino[pk]['current_position'] = crazy_arduino[pk]['next_position']
            board[cr][cc] = SPACE
        for pk, status in crazy_arduino.items():
            ncr, ncc = status['next_position']
            board[ncr][ncc] = CRAZY_ARDUINO
    return board


if __name__ == '__main__':
    # constant
    SPACE, CRAZY_ARDUINO, JONG_SU = '.', 'R', 'I'
    DELTA = {
        1: [1, -1],
        2: [1, 0],
        3: [1, 1],
        4: [0, -1],
        5: [0, 0],
        6: [0, 1],
        7: [-1, -1],
        8: [-1, 0],
        9: [-1, 1]
    }

    # input
    R, C = map(int, input().split())
    BOARD = [list(input()) for _ in range(R)]
    DIRECTION = list(map(int, input()))

    # output
    ANSWER = solve(R, C, BOARD, DIRECTION)
    if type(ANSWER) == list:
        for ROW in ANSWER:
            print(*ROW, sep='')
    elif type(ANSWER) == str:
        print(ANSWER)