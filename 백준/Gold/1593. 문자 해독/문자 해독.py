import sys
input = sys.stdin.readline

# 1593

g, s = map(int, input().split())
W = input().rstrip()
S = input().rstrip()

ans = 0
word_count = [0]*58
sentence_count = [0]*58

for c in W:
    word_count[ord(c)-65] += 1

idx, length = 0, 0
for i in range(s):
    sentence_count[ord(S[i])-65] += 1
    length += 1
    if length == g:
        if word_count == sentence_count:
            ans += 1
        sentence_count[ord(S[idx])-65] -= 1
        idx += 1
        length -= 1
print(ans)