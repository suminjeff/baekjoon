K, N, M = map(int, input().split())
answer = K*N - M
print(answer if answer > 0 else 0)