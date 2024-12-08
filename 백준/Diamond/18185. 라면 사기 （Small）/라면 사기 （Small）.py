import sys


def solve(n: int, data: list[int]) -> int:
    answer = 0

    for i in range(n):
        if data[i+1] > data[i+2]:
            buy2 = min(data[i], data[i+1] - data[i+2])
            answer += 5 * buy2
            data[i] -= buy2
            data[i+1] -= buy2

            buy3 = min(data[i], min(data[i+1], data[i+2]))
            answer += 7 * buy3
            data[i] -= buy3
            data[i+1] -= buy3
            data[i+2] -= buy3
        else:
            buy3 = min(data[i], min(data[i+1], data[i+2]))
            answer += 7 * buy3
            data[i] -= buy3
            data[i+1] -= buy3
            data[i+2] -= buy3

            buy2 = min(data[i], data[i+1])
            answer += 5 * buy2
            data[i] -= buy2
            data[i+1] -= buy2
        answer += 3 * data[i]

    return answer


if __name__ == '__main__':
    N = int(input())
    RAMEN = list(map(int, input().split()))
    DATA = [0]*100000
    for i in range(N):
        DATA[i] = RAMEN[i]
    ANSWER = solve(N, DATA)
    print(ANSWER)