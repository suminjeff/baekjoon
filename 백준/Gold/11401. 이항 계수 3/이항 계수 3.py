import sys


MOD = 1_000_000_007


def mod_inv(a, p):
    return pow(a, p-2, p)


def factorial_mod(n, p):
    fact = [1]*(n+1)
    for i in range(2, n+1):
        fact[i] = fact[i-1]*i % p
    return fact


def binomial_coefficient_mod(n, k, p):
    if k > n or k < 0:
        return 0
    fact = factorial_mod(n, p)
    numerator = fact[n]
    denominator = (fact[k]*fact[n-k]) % p
    denominator_inv = mod_inv(denominator, p)
    return (numerator * denominator_inv) % p


def solve(n, k):
    result = binomial_coefficient_mod(n, k, MOD)
    return result


if __name__ == '__main__':
    N, K = map(int, input().split())
    answer = solve(N, K)
    print(answer)
