N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for col in range(M):
        A[row][col] += B[row][col]


for n in range(N):
    print(*A[n])