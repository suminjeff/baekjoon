import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def find_palindrome_prime(n: int) -> int:
    while True:
        if is_prime(n) and is_palindrome(n):
            return n
        n += 1


if __name__ == "__main__":
    N = int(input())
    print(find_palindrome_prime(N))