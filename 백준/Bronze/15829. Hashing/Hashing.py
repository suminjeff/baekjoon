import sys
input = sys.stdin.readline


def f(string, L):
    r, M = 31, 1234567891
    res = 0
    for i in range(L):
        a = string[i]
        res += (ord(a)-96) * r**i
    return int(res) % M


L = int(input())
string = input().rstrip()
print(f(string, L))