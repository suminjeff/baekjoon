import sys
from math import floor
from collections import deque



class User:
    def __init__(self):
        self.position = []
        self.passed_turns = 0
        self.level = 1
        self.hp_full = 20
        self.hp_current = 20
        self.attack = 2
        self.defense = 2
        self.exp_full = 5
        self.exp_current = 0
        self.killed_by = ""
        self.item = {
            'W': 0,
            'A': 0,
            'O': 0,
        }
        self.ornaments = {
            'HR': False,
            'RE': False,
            'CO': False,
            'EX': False,
            'DX': False,
            'HU': False,
            'CU': False,
        }
        self.game_over_message = "Press any key to continue."

    def gain_exp(self, exp):
        # EX 장신구가 있다면 1.2배
        if self.ornaments['EX'] is True:
            exp = floor(exp*1.2)
        # 경험치를 얻고 레벨업이 안된다면
        if self.exp_current + exp < self.exp_full:
            self.exp_current += exp
        # 레벨업을 한다면
        else:
            self.exp_current = 0
            self.level += 1
            self.exp_full = 5 * self.level
            self.hp_full += 5
            self.attack += 2
            self.defense += 2
            self.hp_current = self.hp_full

    def can_continue(self, killed_by):
        # 만약 RE 장신구가 있다면 가능
        if self.ornaments['RE'] is True:
            self.ornaments['RE'] = False
            self.item['O'] -= 1
            self.hp_current = self.hp_full
            self.position = start_location
            return True
        # 불가능
        else:
            self.hp_current = 0
            self.killed_by = killed_by
            self.game_over_message = f"YOU HAVE BEEN KILLED BY {self.killed_by}.."
            return False

    def win_battle(self, position, exp):
        self.position = position
        self.gain_exp(exp)
        if self.ornaments['HR'] is True:
            self.hp_current = self.hp_current + 3 if self.hp_current + 3 <= self.hp_full else self.hp_full

    def print_result(self, grid):
        for row in grid:
            print(*row, sep='')
        print(f"Passed Turns : {self.passed_turns}")
        print(f"LV : {self.level}")
        print(f"HP : {self.hp_current}/{self.hp_full}")
        print(f"ATT : {self.attack}+{self.item['W']}")
        print(f"DEF : {self.defense}+{self.item['A']}")
        print(f"EXP : {self.exp_current}/{self.exp_full}")
        print(self.game_over_message)


def game_start(grid, moves):
    # 주인공 이동 실행
    while moves:
        move = moves.popleft()
        # 새로 이동할 곳
        r, c = user.position
        dr, dc = MOVE_DELTA_MAP[move]
        nr, nc = r + dr, c + dc
        # N x M 범위 안에 없으면 제자리
        if nr < 0 or nr >= N or nc < 0 or nc >= M or grid[nr][nc] == '#':
            nr, nc = r, c
        user.passed_turns += 1
        # 새 위치가
        # 빈 칸이라면
        if grid[nr][nc] == '.':
            # 이동
            user.position = [nr, nc]
            continue

        # 아이템 상자라면
        elif grid[nr][nc] == 'B':
            item_type, item_effect = ITEM_GRID_MAP[(nr, nc)]['TYPE'], ITEM_GRID_MAP[(nr, nc)]['EFFECT']
            # 무기나 방어구라면
            if item_type == 'W' or item_type == 'A':
                user.item[item_type] = item_effect
            # 장신구라면
            elif item_type == 'O':
                if user.item[item_type] < 4 and user.ornaments[item_effect] is False:
                    user.item[item_type] += 1
                    user.ornaments[item_effect] = True
            # 아이템 상자를 빈칸으로 만들고 이동
            grid[nr][nc] = '.'
            user.position = [nr, nc]
            continue

        # 가시 함정이라면
        elif grid[nr][nc] == '^':
            # 이동
            user.position = [nr, nc]
            spike_damage = 5
            # DX 장신구가 있다면 가시 데미지가 1로 고정
            if user.ornaments['DX'] is True:
                spike_damage = 1
            # 가시를 밟고도 살아있다면
            if user.hp_current > spike_damage:
                user.hp_current -= spike_damage
            # 가시를 밟고 죽는다면
            else:
                # 만약 RE 장신구가 있다면 부활
                if not user.can_continue("SPIKE TRAP"):
                    user.print_result(grid)
                    return

        # 몬스터라면
        elif grid[nr][nc] == '&' or grid[nr][nc] == 'M':
            boss_battle = grid[nr][nc] == 'M'
            monster = MONSTER_GRID_MAP[(nr, nc)]
            monster_original_hp = monster['HP']
            first_attack = True  # 전투 턴
            first_boss_damage = False
            # 보스 몬스터와의 전투에서 HU 장신구가 있다면 최대 체력 회복
            if boss_battle is True and user.ornaments['HU'] is True:
                user.hp_current = user.hp_full
                first_boss_damage = True

            while True:
                # 주인공 먼저 공격
                attack_damage = user.attack + user.item['W']  # 주인공의 기본 공격력 + 아이템 공격력

                # CO 장신구 효과: 공격력 2배
                if first_attack is True and user.ornaments['CO'] is True:
                    # DX 장신구와 함께 사용한다면 공격력 3배
                    if user.ornaments['DX'] is True:
                        attack_damage *= 3
                    else:
                        attack_damage *= 2
                    first_attack = False

                # 주인공의 공격력
                user_attack = max(1, attack_damage-monster['DEF'])
                monster['HP'] -= user_attack  # 주인공이 몬스터를 공격
                # 몬스터가 죽었다면
                if monster['HP'] <= 0:
                    user.win_battle([nr, nc], monster['EXP'])
                    # 만약 보스 몬스터를 처치했다면 게임 종료
                    if boss_battle is True:
                        grid[nr][nc] = '@'
                        user.game_over_message = "YOU WIN!"
                        user.print_result(grid)
                        return
                    grid[nr][nc] = '.'
                    break
                # 몬스터 공격 차례
                # 몬스터의 공격
                monster_attack = max(1, monster['ATT'] - (user.defense + user.item['A']))
                # 보스 몬스터와의 전투에서 HU 장신구가 있다면 첫 공격에 0의 데미지
                if first_boss_damage is True and user.ornaments['HU'] is True:
                    first_boss_damage = False
                    monster_attack = 0

                user.hp_current -= monster_attack
                # 주인공이 죽었다면
                if user.hp_current <= 0:
                    # 만약 RE 장신구가 있다면 부활
                    can_continue = user.can_continue(monster['NAME'])
                    if can_continue is False:
                        monster['HP'] = monster_original_hp
                        user.print_result(grid)
                        return
                    break
    r, c = user.position
    grid[r][c] = '@'
    user.print_result(grid)
    return

if __name__ == "__main__":
    user = User()  # 주인공 생성
    start_location = []
    N, M = map(int, input().split())  # N: 행, M: 열
    K, L = 0, 0  # K: 몬스터 개수, L: 아이템 개수

    # 그리드 생성
    GRID = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if GRID[r][c] == '&' or GRID[r][c] == 'M':
                K += 1
            elif GRID[r][c] == 'B':
                L += 1
            elif GRID[r][c] == '@':
                user.position = [r, c]
                start_location = [r, c]
                GRID[r][c] = '.'

    # 주인공 이동 리스트
    MOVES = deque(list(input()))
    MOVE_DELTA_MAP = {
        'L': [0, -1],
        'R': [0, 1],
        'U': [-1, 0],
        'D': [1, 0],
    }

    # 몬스터-그리드 매핑
    MONSTER_GRID_MAP = {}
    for _ in range(K):
        R, C, S, W, A, H, E = input().split()
        MONSTER_GRID_MAP[(int(R)-1, int(C)-1)] = {
            'NAME': S,
            'ATT': int(W),
            'DEF': int(A),
            'HP': int(H),
            'EXP': int(E),
        }

    # 아이템-그리드 매핑
    ITEM_GRID_MAP = {}
    for _ in range(L):
        R, C, T, S = input().split()
        ITEM_GRID_MAP[(int(R)-1, int(C)-1)] = {
            'TYPE': T,
            'EFFECT': int(S) if T in ['W', 'A'] else S,
        }

    game_start(GRID, MOVES)
