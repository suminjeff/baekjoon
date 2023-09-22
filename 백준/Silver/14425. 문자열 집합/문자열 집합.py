import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {}
for _ in range(N):
    S.setdefault(input().rstrip(), 1)

cnt = 0
for _ in range(M):
    v = S.get(input().rstrip())
    cnt += 0 if v is None else v

print(cnt)