import sys
input = sys.stdin.readline

nA, nB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
nDic = {}
for i in range(max(nA, nB)):
    if i < nA:
        vA = A[i]
        if vA in nDic.keys():
            nDic[vA] += 1
        else:
            nDic[vA] = 1
    if i < nB:
        vB = B[i]
        if vB in nDic.keys():
            nDic[vB] += 1
        else:
            nDic[vB] = 1
cnt = 0
for k, v in nDic.items():
    if v == 1:
        cnt += 1
print(cnt)