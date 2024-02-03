import sys
input = sys.stdin.readline

# 6064


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)


def lcm(x, y):
    return (x * y) // gcd(x, y)


T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    ans, max_year = x, lcm(m, n)
    while ans <= max_year:
        if (ans-1) % n + 1 == y:
            break
        ans += m
    if ans > max_year:
        print(-1)
    else:
        print(ans)