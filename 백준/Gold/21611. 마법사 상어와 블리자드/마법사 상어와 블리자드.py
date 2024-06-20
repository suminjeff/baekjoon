import sys


def get_blizzard_index_list(n):
    # 인덱스를 큰 것부터 거꾸로 해야 의도대로 pop을 할 수 있음
    # 1: 상, 2: 하, 3: 좌, 4: 우
    blizzard_index_list = {
        1: [(x ** 2 - (x - 1) // 2 - 1) for x in range(n, 2, -2)],
        2: [((x - 1) ** 2 - (x - 1) // 2) for x in range(n, 2, -2)],
        3: [(x ** 2 + (x - 1) // 2) for x in range(n-2, 0, -2)],
        4: [((x - 1) ** 2 + (x - 1) // 2) for x in range(n, 2, -2)],
    }
    return blizzard_index_list


def get_marble_list(n, marbles):
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    marble_list = []
    sr, sc = (n-1)//2, (n-1)//2
    marble_list.append(marbles[sr][sc])
    r, c = sr, sc-1
    ring_size = 3
    while 0 <= r < n and 0 <= c < n:
        distance = ring_size - 1
        for d in range(4):
            dr, dc = delta[d]
            if d != 0:
                r, c = r+dr, c+dc
            for nr, nc in [(r+dr*x, c+dc*x) for x in range(distance)]:
                if 0 <= nr < n and 0 <= nc < n:
                    marble = marbles[nr][nc]
                    if marble > 0:
                        marble_list.append(marbles[nr][nc])
                        r, c = nr, nc
                    else:
                        return marble_list
        c -= 1
        ring_size += 2
    return marble_list


def get_chain_explosion_index_list(marble_list):
    marble_list_size = len(marble_list)
    chain_explosion_index_list = []
    chain_number, chain_size, chain_index_list = 0, 1, []
    for index in range(1, marble_list_size):
        marble_number = marble_list[index]
        if index == 1:
            chain_number = marble_number
            chain_index_list.append(index)
        else:
            if marble_number == chain_number:
                chain_size += 1
                chain_index_list.append(index)
            else:
                if chain_size >= 4:
                    chain_explosion_index_list.extend(chain_index_list)
                chain_number = marble_number
                chain_size = 1
                chain_index_list.clear()
                chain_index_list.append(index)
    if chain_size >= 4:
        chain_explosion_index_list.extend(chain_index_list)
    return chain_explosion_index_list


def get_marble_group_list(marble_list):
    marble_list_size = len(marble_list)
    marble_group_list = []
    group_number, group_size, group_index_list = 0, 1, []
    for index in range(1, marble_list_size):
        marble_number = marble_list[index]
        if index == 1:
            group_number = marble_number
            group_index_list.append(index)
            continue
        if marble_number == group_number:
            group_size += 1
            group_index_list.append(index)
        else:
            group = {
                'number': group_number,
                'size': group_size,
                'index_list': group_index_list[:]
            }
            marble_group_list.append(group)
            group_number = marble_number
            group_size = 1
            group_index_list.clear()
            group_index_list.append(index)
    final_group = {
        'number': group_number,
        'size': group_size,
        'index_list': group_index_list[:]
    }
    marble_group_list.append(final_group)
    return marble_group_list


def solve(n, m, marbles, blizzard):
    blizzard_index_list = get_blizzard_index_list(n)
    marble_list = get_marble_list(n, marbles)
    if len(marble_list) < 2:
        return 0
    explosion = {x: 0 for x in range(1, 4)}  # 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)
    for d, s in blizzard:
        index_list = blizzard_index_list[d][((n-1)//2)-s:]  # (n-1)//2 - s: 범위의 최대값
        # 1. 블리자드 마법 시전, 구슬 파괴
        for index in index_list:
            if index < len(marble_list):
                marble_list.pop(index)

        # 2. 4개 이상 연속하는 구슬 폭발, 연쇄 폭발이 끝날 때까지
        while True:
            chain_explosion_index_list = get_chain_explosion_index_list(marble_list)
            if not chain_explosion_index_list:
                break
            while chain_explosion_index_list:
                index = chain_explosion_index_list.pop()
                marble_number = marble_list[index]
                explosion[marble_number] += 1
                if index < len(marble_list):
                    marble_list.pop(index)
        if len(marble_list) < 2:
            break
        # 3. 구슬 변화, A: 그룹에 들어 있는 구슬의 개수, B: 그룹을 이루고 있는 구슬의 번호
        marble_group_list = get_marble_group_list(marble_list)
        while marble_group_list:
            group = marble_group_list.pop()
            number, size, index_list = group['number'], group['size'], group['index_list']
            starting_index = index_list[0]
            while len(index_list) > 1:
                index = index_list.pop()
                marble_list.pop(index)
            marble_list.insert(starting_index+1, number)
            marble_list.insert(starting_index+1, size)
            marble_list.pop(starting_index)
        # 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다
        marble_list_size = len(marble_list)
        if marble_list_size > n**2:
            while marble_list_size > n**2-1:
                marble_list.pop()
                marble_list_size -= 1
    result = [x*explosion[x] for x in range(1, 4)]
    answer = sum(result)
    return answer



if __name__ == '__main__':
    N, M = map(int, input().split())
    MARBLES = [list(map(int, input().split())) for _ in range(N)]
    BLIZZARD = [list(map(int, input().split())) for _ in range(M)]
    answer = solve(N, M, MARBLES, BLIZZARD)
    print(answer)