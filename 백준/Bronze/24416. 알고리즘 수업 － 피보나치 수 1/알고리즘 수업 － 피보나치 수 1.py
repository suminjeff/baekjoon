import sys
input = sys.stdin.readline


def recursive_fibo(n):
    if n == 1 or n == 2:
        return 1
    return recursive_fibo(n-1) + recursive_fibo(n-2)


def dp_fibo(n):
    global dp_cnt
    fibo = [0] * (n+1)
    fibo[1] = fibo[2] = 1
    for i in range(3, n+1):
        dp_cnt += 1
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]


N = int(input())
dp_cnt = 0
d_fibo = dp_fibo(N)
print(d_fibo, dp_cnt)