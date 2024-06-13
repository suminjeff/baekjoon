import sys
from collections import Counter


def r_sort(arr, size):
    new_arr = [[] for _ in range(size)]
    max_size = 0
    for r in range(size):
        row = arr[r]
        row_count = Counter(row)
        for key, value in sorted(row_count.items(), key=lambda x:(x[1],x[0])):
            if key == 0:
                continue
            new_arr[r].extend([key, value])
        max_size = max(max_size, len(new_arr[r]))
    for r in range(size):
        diff = max_size - len(new_arr[r])
        new_arr[r].extend([0]*diff)

    return new_arr


def c_sort(arr, size):
    transposed_arr = list(map(list, zip(*arr))) # 전치 행렬
    new_arr = r_sort(transposed_arr, size)
    new_arr = list(map(list, zip(*new_arr)))
    return new_arr




def solve(row: int, column: int, value: int, arr: list):
    answer = 0

    while answer <= 100:
        R, C = len(arr), len(arr[0])
        if R > row and C > column and arr[row][column] == value:
            return answer
        if R >= C:
            arr = r_sort(arr, R)
        else:
            arr = c_sort(arr, C)
        answer += 1

    return -1



def main():
    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]
    answer = solve(r-1, c-1, k, A)
    print(answer)
    return


if __name__ == '__main__':
    main()