import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hear = {}
cnt = 0
ans = []
for i in range(N+M):
    name = input().rstrip()
    if 0 <= i < N:
        hear[name] = 1
    elif N <= i < N+M:
        if name in hear.keys():
            cnt += 1
            ans.append(name)
ans.sort()
print(cnt)
print(*ans, sep="\n")