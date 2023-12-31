import sys
input = sys.stdin.readline

S = input().rstrip()
cache = [[0]*len(S) for _ in range(26)]
cache[ord(S[0])-97][0] += 1
for i in range(1, len(S)):
    s = ord(S[i])-97
    cache[s][i] += 1
    for j in range(26):
        cache[j][i] += cache[j][i-1]
q = int(input())
for _ in range(q):
    alphabet, left, right = input().rstrip().split()
    alphabet, left, right = ord(alphabet)-97, int(left), int(right)
    if left > 0:
        res = cache[alphabet][right] - cache[alphabet][left-1]
    else:
        res = cache[alphabet][right]
    print(res)