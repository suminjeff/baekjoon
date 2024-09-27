from itertools import combinations


def solve(n, m, arr):
    arr.sort()
    checker = set()
    answer = []
    for combination in combinations(arr, m):
        if combination not in checker:
            checker.add(combination)
            answer.append(combination)

    return answer



if __name__ == '__main__':
    N, M = map(int, input().split())
    ARR = list(map(int, input().split()))
    ANSWER = solve(N, M, ARR)
    for SEQUENCE in ANSWER:
        print(*SEQUENCE)