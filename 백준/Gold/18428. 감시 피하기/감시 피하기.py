import sys
sys.setrecursionlimit(10**5)


def solve(n: int, grid: list[list[str]]):

    def find(target):
        result = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == target:
                    result.append([i, j])
        return result

    def backtrack(depth):
        nonlocal answer
        if depth == LIMIT:
            if not teacher_find_student():
                answer = YES
            return
        for i in range(n):
            for j in range(n):
                if grid[i][j] == SPACE:
                    grid[i][j] = OBSTACLE
                    backtrack(depth + 1)
                    grid[i][j] = SPACE

    def teacher_find_student():
        for r, c in teachers:
            for d in range(4):
                dr, dc = DELTA[d]
                nr, nc = r+dr, c+dc
                while 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == OBSTACLE:
                        break
                    if grid[nr][nc] == STUDENT:
                        return True
                    nr, nc = nr + dr, nc + dc
        return False

    teachers = find(TEACHER)
    answer = NO
    backtrack(0)
    return answer


if __name__ == '__main__':
    # const
    LIMIT = 3
    DELTA = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    YES, NO = 'YES', 'NO'
    TEACHER, STUDENT, OBSTACLE, SPACE = 'T', 'S', 'O', 'X'

    # input
    N = int(input())
    GRID = [list(input().split()) for _ in range(N)]

    # answer
    ANSWER = solve(N, GRID)
    print(ANSWER)