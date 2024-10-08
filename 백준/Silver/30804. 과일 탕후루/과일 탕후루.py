import sys
from collections import defaultdict


def solve(n: int, s: list):
    answer = 0

    left, right = 0, 0
    kind = 0
    counter = defaultdict(int)

    while right < n:
        if counter[s[right]] == 0:
            kind += 1
        counter[s[right]] += 1

        while kind > 2:
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                kind -= 1
            left += 1

        answer = max(answer, right - left + 1)
        right += 1

    return answer


if __name__ == '__main__':
    # const

    # input
    N = int(input())
    S = list(map(int, input().split()))

    # answer
    ANSWER = solve(N, S)
    print(ANSWER)