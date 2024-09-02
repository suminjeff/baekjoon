import sys


def solve(n, s, sequence):
    inf = sys.maxsize
    answer = inf
    start, end = 0, 0
    min_v = sequence[0]

    while True:
        if min_v < S:
            end += 1
            if end == N:
                break
            min_v += sequence[end]
        else:
            answer = min(answer, end-start+1)
            min_v -= sequence[start]
            start += 1
    answer = 0 if answer == inf else answer
    return answer


if __name__ == '__main__':
    N, S = map(int, input().split())
    SEQUENCE = list(map(int, input().split()))
    ANSWER = solve(N, S, SEQUENCE)
    print(ANSWER)