import sys

def solve(n):
    length = n//2

    for i in range(n-3, 2, -2):
        if is_prime[i] and is_prime[n-i]:
            return f'{n} = {n-i} + {i}'

    return "Goldbach's conjecture is wrong."




if __name__ == '__main__':
    is_prime = [True]*1000001

    for i in range(2, int(1000001**0.5)+1):
        if is_prime[i]:
            for j in range(2*i, 1000001, i):
                is_prime[j] = False


    while True:
        N = int(input())
        if N == 0:
            break
        ANSWER = solve(N)
        print(ANSWER)
