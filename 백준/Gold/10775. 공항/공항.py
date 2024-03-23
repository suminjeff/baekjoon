import sys
input = sys.stdin.readline


# 10775

G = int(input())
P = int(input())

cnt = 0


def find(x):
    if gates[x] == -1:
        return x

    if gates[x] != x:
        gates[x] = find(gates[x])
    return gates[x]


def union(x, y):
    p, q = find(x), find(y)
    if p == q:
        return
    gates[q] = p


gates = [-1 for i in range(G+1)]
ans = 0
for i in range(P):
    plane = int(input())
    gate = find(plane)
    if gate == 0:
        break
    union(gate-1, gate)
    ans += 1
print(ans)