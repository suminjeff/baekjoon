import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def factorial(n, depth, target):
    if depth == target:
        return n
    return n * factorial(n-1, depth+1, target)


def nCr(n, r):
    if r == 0:
        return 1
    return factorial(n, 1, r)//factorial(r, 1, r)


N, K = map(int, input().split())
print(nCr(N, K))
