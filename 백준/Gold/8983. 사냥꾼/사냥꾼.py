import sys

from heapq import heappop, heappush


def get_distance(x, a, b):
    return abs(x-a) + b


if __name__ == '__main__':
    M, N, L = map(int, input().split())
    guns = list(map(int, input().split()))
    animals = [list(map(int, input().split())) for _ in range(N)]
    killed = [0]*N

    for i in range(M):
        x = guns[i]
        distance = [get_distance(x, a, b) for a, b in animals]
        pop_index = []
        for j in range(N):
            if distance[j] <= L:
                pop_index.append(j)
                killed[i] += 1
        while pop_index:
            idx = pop_index.pop()
            animals.pop(idx)
            N -= 1
    answer = sum(killed)
    print(answer)