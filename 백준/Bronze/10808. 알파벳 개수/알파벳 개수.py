counts = [0]*26
S = input()
for i in range(len(S)):
    s = S[i]
    n = ord(s)-97
    counts[n] += 1
print(*counts)