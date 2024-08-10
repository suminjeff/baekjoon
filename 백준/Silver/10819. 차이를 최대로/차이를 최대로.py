from itertools import permutations


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    max_v = 0
    for perm in permutations(A, N):
        v = sum([abs(perm[i]-perm[i+1]) for i in range(N-1)])
        max_v = max(max_v, v)
    print(max_v)