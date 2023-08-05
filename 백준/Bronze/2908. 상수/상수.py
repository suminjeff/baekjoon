A, B = map(str, input().split())
A = int(A[::-1])
B = int(B[::-1])

max_v = A
if A < B:
    max_v = B
print(max_v)