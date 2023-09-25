import sys
input = sys.stdin.readline

N, M = map(int, input().split())
voca = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    if word in voca.keys():
        voca[word] += 1
    else:
        voca.setdefault(word, 1)
ans = sorted(voca.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in ans:
    print(i[0])