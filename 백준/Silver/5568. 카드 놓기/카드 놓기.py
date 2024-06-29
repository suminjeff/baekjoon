import sys
input = sys.stdin.readline


def dfs(i, depth, number):
    if depth == K:
        NUMBERS.add(number)
        return

    for ni in range(N):
        if VISITED[ni] == 0:
            VISITED[ni] = 1
            dfs(ni, depth+1, number+str(CARDS[ni]))
            VISITED[ni] = 0


N = int(input())
K = int(input())
CARDS = [int(input()) for _ in range(N)]
VISITED = [0]*N
NUMBERS = set()
dfs(0, 0, "")
ANSWER = len(NUMBERS)
print(ANSWER)