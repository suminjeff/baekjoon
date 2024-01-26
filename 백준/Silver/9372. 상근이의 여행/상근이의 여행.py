import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    planes = [list(map(int, input().split())) for _ in range(M)]
    print(N-1)