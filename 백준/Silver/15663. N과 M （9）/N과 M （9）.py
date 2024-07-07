import sys


def dfs(depth, sequence):
    if depth == M:
        result.add(tuple(sequence))
        return
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            sequence.append(numbers[i])
            dfs(depth+1, sequence)
            visited[i] = False
            sequence.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False] * N

result = set()

dfs(0, [])

answer = sorted(list(result))
for seq in answer:
    print(*seq)