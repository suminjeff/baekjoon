import sys


def solve(n, liquid):
    liquid.sort()

    left, right = 0, n-1
    _min = sys.maxsize
    _l, _r = -1, -1
    while left < right:
        _sum = liquid[left]+liquid[right]
        if _min > abs(_sum):
            _min = abs(_sum)
            _l, _r = left, right
            if _sum == 0:
                break
                
        if _sum < 0:
            left += 1
        else:
            right -= 1

    return liquid[_l], liquid[_r]


if __name__ == '__main__':
    N = int(input())
    LIQUID = list(map(int, input().split()))
    ANSWER = solve(N, LIQUID)
    print(*ANSWER)