import sys
input = sys.stdin.readline

def star(n):
    for i in range(1, n+1):
        print((' ' * (n - i)) + ('*' * (2*i-1)))

N = int(input())
star(N)