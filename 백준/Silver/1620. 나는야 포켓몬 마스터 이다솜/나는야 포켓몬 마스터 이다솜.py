import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pkm_by_name = {}
pkm_by_id = {}
for i in range(1, N+1):
    name = input().rstrip()
    pkm_by_name[name] = i
    pkm_by_id[i] = name
for _ in range(M):
    q = input().rstrip()
    if q.isnumeric():
        print(pkm_by_id[int(q)])
    else:
        print(pkm_by_name[q])