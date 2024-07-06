import sys

INF = sys.maxsize
N, M = map(int, input().split())
pack, single = INF, INF

for _ in range(M):
    p, s = map(int, input().split())
    pack, single = min(pack, p), min(single, s)

if pack > single*6:
    pack = single*6

buy_pack, buy_single = divmod(N, 6)

answer = min(buy_pack*pack + buy_single*single, (buy_pack+1)*pack)

print(answer)