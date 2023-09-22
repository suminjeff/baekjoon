import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)
subsets = set()
subsets.add(S)
for i in range(N):
    subsets.add(S[i])
for i in range(N):
    ss = S[i]
    for j in range(i+1, N):
        ss += S[j]
        subsets.add(ss)
print(len(subsets))